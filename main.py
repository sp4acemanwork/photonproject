def start_game_with_countdown(parent, event=None):
    from countdown_timer import CountdownTimer  # Import inside function
    CountdownTimer(parent, countdown_to_playaction)

def countdown_to_playaction():
    # self.app.destroy()
    print("Countdown finished, switching to ActionFrame screen...")
    # New window initialized
    from window import window, actionFrame, actionFrame2  # Import inside function
    test = window()
    testpage = actionFrame(test.window, test)
    testpage2 = actionFrame2(test.window, test)
    test.addPage("actionscreen", testpage)
    test.addPage("test", testpage2)
    test.redraw("actionscreen")
    # testpage.append_list(self.list_of_id_and_names)

def main():
    from splash_screen import SplashScreen  # Import inside function
    splash_root = SplashScreen()
    splash_root.after(3000, splash_root.splash_root.next_screen)
    splash_root.mainloop()

if __name__ == "__main__":
    main()