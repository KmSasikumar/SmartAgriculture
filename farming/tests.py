from django.contrib.auth.models import User
from django.test import TestCase

from .models import calculate_yeild, crop_productions

PW = "Test@1234"


class PublicPagesTests(TestCase):
    def test_public_pages_render(self):
        for url in ["/", "/sign/", "/register/", "/cropHealth/",
                    "/article1/", "/article2/", "/article3/",
                    "/soilClassification/", "/soilType/"]:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)

    def test_home_article_links_use_routes(self):
        body = self.client.get("/").content.decode()
        self.assertNotIn('href="article 1.html"', body)
        self.assertIn("/article1/", body)


class CalculatorTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="farmer1", password=PW, email="f1@example.com")
        self.client.force_login(self.user)

    def test_yield_valid(self):
        r = self.client.post("/cropyeild/", {"weight": "1000", "area": "4"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(calculate_yeild.objects.last().result, 250.0)

    def test_yield_fraction_is_not_truncated(self):
        self.client.post("/cropyeild/", {"weight": "403", "area": "4"})
        self.assertAlmostEqual(calculate_yeild.objects.last().result, 100.75)

    def test_yield_zero_area_does_not_500(self):
        r = self.client.post("/cropyeild/", {"weight": "100", "area": "0"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("greater than zero", r.content.decode())

    def test_yield_non_numeric_does_not_500(self):
        r = self.client.post("/cropyeild/", {"weight": "abc", "area": "2"})
        self.assertEqual(r.status_code, 200)

    def test_production_valid_with_decimal_yield(self):
        r = self.client.post("/production/", {
            "crop_name": "Rice", "land_acer": "2", "crop-yield": "100.5",
            "user_cost": "500", "market_price": "20"})
        self.assertEqual(r.status_code, 200)
        row = crop_productions.objects.last()
        self.assertAlmostEqual(row.totalProduction, 201.0)
        self.assertAlmostEqual(row.profit, 3020.0)

    def test_production_non_numeric_does_not_500(self):
        r = self.client.post("/production/", {
            "crop_name": "Rice", "land_acer": "x", "crop-yield": "1",
            "user_cost": "1", "market_price": "1"})
        self.assertEqual(r.status_code, 200)

    def test_calculators_require_login(self):
        self.client.logout()
        self.assertEqual(self.client.get("/cropyeild/").status_code, 302)
        self.assertEqual(self.client.get("/production/").status_code, 302)
        self.assertEqual(self.client.get("/finance/").status_code, 302)


class AuthFlowTests(TestCase):
    def _register(self, **over):
        data = {"signin": "1", "fname": "New", "lname": "User",
                "username": "newuser", "mail": "new@example.com",
                "password": PW, "confirmpassword": PW}
        data.update(over)
        return self.client.post("/register/", data)

    def test_register_creates_and_logs_in(self):
        r = self._register()
        self.assertTrue(User.objects.filter(username="newuser").exists())
        self.assertEqual(r.status_code, 302)

    def test_register_password_mismatch_shows_error(self):
        r = self._register(confirmpassword="Other@123")
        self.assertFalse(User.objects.filter(username="newuser").exists())
        self.assertIn("do not match", r.content.decode())

    def test_register_duplicate_email_rejected(self):
        User.objects.create_user(username="someone", password=PW,
                                 email="dup@example.com")
        r = self._register(mail="dup@example.com")
        self.assertFalse(User.objects.filter(username="newuser").exists())
        self.assertIn("already registered", r.content.decode())

    def test_register_missing_fields_does_not_500(self):
        r = self.client.post("/register/", {
            "signin": "1", "username": "nofields", "mail": "nf@example.com",
            "password": PW, "confirmpassword": PW})
        self.assertEqual(r.status_code, 200)

    def test_signin_wrong_password_redirects_to_register(self):
        User.objects.create_user(username="farmer1", password=PW)
        r = self.client.post("/sign/", {"Username": "farmer1", "password": "wrong"})
        self.assertEqual(r.status_code, 302)
