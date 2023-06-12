import json
from typing import Any

from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button.button import MDFlatButton
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager

Window.size = (360, 640)


def show_dialog(title: str, message: str):
    dialog = MDDialog(
        title=title,
        text=message,
        buttons=[
            MDFlatButton(
                text="Close", on_release=lambda *x: dialog.dismiss()  # type:ignore
            )
        ],
    )
    dialog.open()


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

    def on_register_success(self, req: UrlRequest, result: dict[str, Any]):
        message = result.get("error", "Registration Successful. Welcome to the Hub!")
        show_dialog("Success", message)

        # Clear MDTextFields
        self.ids.name_field.text = ""
        self.ids.username_field.text = ""
        self.ids.password_field.text = ""

        # Switch to main.kv Screen
        self.manager.transition.direction = "left"
        self.manager.current = "main"

    def on_register_failure(self):
        show_dialog("Error", "Failed to register account")

    def review_credentials(self):
        show_dialog("Error", "Enter your credentials first!")


class LoginScreen(Screen):
    def login(self):
        username, password = (
            self.ids.username_field.text,
            self.ids.password_field.text,
        )

        if not all([username, password]):
            show_dialog("Error", "Enter your credentials first!")
            return

        UrlRequest(
            url="http://127.0.0.1:5000/auth/login",
            req_body=json.dumps({"username": username, "password": password}),
            req_headers={"Content-Type": "application/json"},
            on_success=self.login_success,
            on_failure=self.login_failure,
        )

    def login_success(self, request: UrlRequest, result: dict[str, str]):
        self.ids.username_field.text = ""

        print("Login successful")
        # user_id = result.get("id")
        # username = result.get("username")
        show_dialog("Success", "Welcome Back!")
        self.manager.transition.direction = "left"
        self.manager.current = "main"

    def login_failure(self, request: UrlRequest, result: str):
        show_dialog("Error", "Invalid credentials. Username and Password do not match!")


class MainScreen(Screen):
    def on_enter(self, *args: Any):
        super().on_enter(*args)  # type: ignore

        self.load_recipes()

    def load_recipes(self):
        UrlRequest(
            url="http://127.0.0.1:5000/api/recipes",
            on_success=self.on_load_recipes_success,
            on_failure=self.on_load_recipes_failure,
        )

    def on_load_recipes_success(self, req: UrlRequest, result: Any):
        recipe_layout = self.ids.recipes_layout
        for recipe in result["Recipes"]:
            print(recipe)

            recipe_card = Builder.load_file("components/recipe_card.kv")
            if not recipe_card:
                continue
            recipe_card.ids.title.text = recipe["name"]
            recipe_card.ids.ingredients.text = recipe["ingredients"]
            recipe_card.ids.instructions.text = recipe["instructions"]

            recipe_layout.add_widget(recipe_card)

    def on_load_recipes_failure(self, req: UrlRequest, result: Any):
        show_dialog("Error", "Failed to load recipes")

    def logout(self):
        show_dialog("Success", "Signed out successfully")
        self.manager.transition.direction = "right"
        self.manager.current = "login"

    def add_recipe(self):
        recipe_name = self.ids.recipe_name.text
        recipe_ingredients = self.ids.recipe_ingredients.text
        recipe_instructions = self.ids.recipe_instructions.text

        if not all([recipe_name, recipe_ingredients, recipe_instructions]):
            show_dialog("Error", "Enter all the recipe details!")
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

    def on_add_recipe_success(self, req: UrlRequest, result: dict[str, Any]):
        message = result.get("message", "Recipe added successfully!")
        show_dialog("Success", message)

        # Clear MDTextFields
        self.ids.recipe_name.text = ""
        self.ids.recipe_ingredients.text = ""
        self.ids.recipe_instructions.text = ""

    def on_add_recipe_failure(self):
        show_dialog("Error", "Failed to add recipe")


if __name__ == "__main__":
    LabelBase.register(  # type:ignore
        name="Gagalin", fn_regular="assets/fonts/Gagalin-Regular.ttf"
    )
    MainApp().run()
