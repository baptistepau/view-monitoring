from FirefoxControl import FirefoxControl

def main():
    controler = FirefoxControl("conf_file.json")
    controler.start()

if __name__ == '__main__':
    main()
