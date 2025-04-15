from window import window, splashFrame, actionFrame, playerFrame

teams = None


def main():
    # from splash_screen import SplashScreen
    # splash_root = SplashScreen()
    # splash_root.after(3000, splash_root.splash_root.next_screen)
    # splash_root.mainloop()
    parent = window()
    splash_frame = splashFrame(parent)
    action_frame = actionFrame(parent)
    player_frame = playerFrame(parent)
    parent.addPage("playerscreen", splash_frame)
    parent.addPage("actionframe", action_frame)
    parent.addPage("playerframe", player_frame)
    parent.redraw_intital("playerscreen")
    parent.window.mainloop()


if __name__ == "__main__":
    main()

