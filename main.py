from splash_screen import SplashScreen

def main():
    
    splash_root = SplashScreen()
    splash_root.after(3000, splash_root.splash_root.next_screen)
    splash_root.mainloop()

if __name__ == "__main__":
    main()