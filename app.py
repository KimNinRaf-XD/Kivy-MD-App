import json

from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button.button import MDFlatButton
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager

Window.size = (360, 640)


class MainApp(MDApp):
    def build(self):
        screen_manager = MDScreenManager()

        Builder.load_file("screens/welcome.kv")
        Builder.load_file("screens/auth/login.kv")
        Builder.load_file("screens/auth/signup.kv")
        Builder.load_file("screens/main.kv")

        screen_manager.add_widget(WelcomeScreen(name="welcome"))
        screen_manager.add_widget(LoginScreen(name="login"))
        screen_manager.add_widget(SignupScreen(name="signup"))
        screen_manager.add_widget(MainScreen(name="main"))

        return screen_manager


class WelcomeScreen(Screen):
    pass


class SignupScreen(Screen):
    def register_account(self):
        name, username, password = (
            self.ids.name_field.text,
            self.ids.username_field.text,
            self.ids.password_field.text,
        )

        if not all([name, username, password]):
            self.review_credentials()
            return

        UrlRequest(
            url="http://127.0.0.1:5000/api/register",
            req_body=json.dumps(
                {"name": name, "username": username, "password": password}
            ),
            req_headers={"Content-Type": "application/json"},
            on_success=self.on_register_success,
            on_failure=self.on_register_failure,
        )

    def on_register_success(self, req, result):
        message = result.get("error", "Registration Successful. Welcome to the Hub!")
        self.show_dialog("Success", message)

        # Clear MDTextFields
        self.ids.name_field.text = ""
        self.ids.username_field.text = ""
        self.ids.password_field.text = ""

        # Switch to main.kv Screen
        self.manager.transition.direction = "left"
        self.manager.current = "main"

    def on_register_failure(self):
        self.show_dialog("Error", "Failed to register account")

    def review_credentials(self):
        self.show_dialog("Error", "Enter your credentials first!")

    def show_dialog(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            buttons=[
                MDFlatButton(text="Close", on_release=lambda *x: dialog.dismiss())
            ],
        )
        dialog.open()


class LoginScreen(Screen):
    def login(self):
        username, password = (
            self.ids.username_field.text,
            self.ids.password_field.text,
        )

        if not all([username, password]):
            self.show_dialog("Error", "Enter your credentials first!")
            return

        UrlRequest(
            url="http://127.0.0.1:5000/api/accounts",
            on_success=lambda req, result: self.check_credentials(
                result, username, password
            ),
        )

    def check_credentials(self, data, username, password):
        accounts = data.get("Accounts", [])
        for account in accounts:
            if account["username"] == username and account["password"] == password:
                self.show_dialog("Success", "Welcome Back!")
                self.manager.transition.direction = "left"
                self.manager.current = "main"
                return

        self.show_dialog(
            "Error", "Invalid credentials. Username and Password do not match!"
        )

    def show_dialog(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            buttons=[
                MDFlatButton(text="Close", on_release=lambda *x: dialog.dismiss())
            ],
        )
        dialog.open()


class MainScreen(Screen):
    recipe_names = ListProperty([])

    def logout(self):
        self.show_dialog("Success", "Signed out successfully")
        self.manager.transition.direction = "right"
        self.manager.current = "login"

    def add_recipe(self):
        recipe_name = self.ids.recipe_name.text
        recipe_ingredients = self.ids.recipe_ingredients.text
        recipe_instructions = self.ids.recipe_instructions.text

        if not all([recipe_name, recipe_ingredients, recipe_instructions]):
            self.show_dialog("Error", "Enter all the recipe details!")
            return

        UrlRequest(
            url="http://127.0.0.1:5000/api/add-recipe",
            req_body=json.dumps(
                {
                    "name": recipe_name,
                    "ingredients": recipe_ingredients,
                    "instructions": recipe_instructions,
                }
            ),
            req_headers={"Content-Type": "application/json"},
            on_success=self.on_add_recipe_success,
            on_failure=self.on_add_recipe_failure,
        )

    def on_add_recipe_success(self, req, result):
        message = result.get("message", "Recipe added successfully!")
        self.show_dialog("Success", message)

        # Clear MDTextFields
        self.ids.recipe_name.text = ""
        self.ids.recipe_ingredients.text = ""
        self.ids.recipe_instructions.text = ""

    def on_add_recipe_failure(self):
        self.show_dialog("Error", "Failed to add recipe")

    def show_dialog(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            buttons=[
                MDFlatButton(text="Close", on_release=lambda *x: dialog.dismiss())
            ],
        )
        dialog.open()

    # def load_recipes(self):
    #     UrlRequest(
    #         url="http://127.0.0.1:5000/api/recipes",
    #         on_success=self.on_load_recipes_success,
    #         on_failure=self.on_load_recipes_failure,
    #     )

    # def on_load_recipes_success(self, req, result):
    #     recipes = result.get("recipes", [])
    #     self.recipe_names = [recipe["name"] for recipe in recipes]

    # def on_load_recipes_failure(self):
    #     self.show_dialog("Error", "Failed to load recipes")


if __name__ == "__main__":
    LabelBase.register(name="Gagalin", fn_regular="assets/fonts/Gagalin-Regular.ttf")
    MainApp().run()
