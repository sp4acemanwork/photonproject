
teams = None


def main():
    
    # from splash_screen import SplashScreen  
    # splash_root = SplashScreen()
    # splash_root.after(3000, splash_root.splash_root.next_screen)
    # splash_root.mainloop()

    from window import window,splashFrame
    test = window()
    testpage = splashFrame(test.window, test)
    test.addPage("playerscreen", testpage)

    test.redraw("playerscreen")
    test.window.mainloop()

   

if __name__ == "__main__":
    main()