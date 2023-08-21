import Menus.MainMenu as M
from cmdOptions.Tools import Tools

def main():
    os = Tools.get_system_type()
    menu = M.MainMenu(os)

    menu.run()


if __name__ == "__main__":
    main()