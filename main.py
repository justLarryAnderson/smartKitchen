from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

class FridgeScreen(MDScreen):
    pass

class DishesScreen(MDScreen):
    pass

class CartScreen(MDScreen):
    pass

class ProfileScreen(MDScreen):
    pass

class KitchenApp(MDApp):
    def build(self):
        Window.size = (360, 640)
        # Set themese and palet
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palet = 'Teal'
        #Loading all screens, need optimiztion later
        Builder.load_file('screens/cart.kv')
        Builder.load_file('screens/dishes.kv')
        Builder.load_file('screens/fridge.kv')
        Builder.load_file('screens/profile.kv')
        # Create screen_manager
        self.screen_manager = MDScreenManager()
        self.screen_manager.add_widget(FridgeScreen())
        self.screen_manager.add_widget(CartScreen())
        self.screen_manager.add_widget(DishesScreen())
        self.screen_manager.add_widget(ProfileScreen())
        
        return self.screen_manager

if __name__ == '__main__':
    KitchenApp().run()

