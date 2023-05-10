import keep_alive

status = "None"
web = keep_alive.website

choice = "default"
launched = False

def launch():
    global launched
    if not launched:
        if (choice == "slash"):
            import SpikebotSlash
            SpikebotSlash.Spike(web)
        else:
            import Spikebot
            Spikebot.Spike(web)
    launched = True

launch()
#Drakebot.Drake()

