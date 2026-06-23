
shutdown = input("Do you want to shut down your computer?(Y/N):").strip().upper()
def MyShutdown():
    if shutdown == "Y":
        print("Shutting computer down....")
        print("Closing all files....")
        print("Almost there....")
        print("Shutdown complete")
MyShutdown()