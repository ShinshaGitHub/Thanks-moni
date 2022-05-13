init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="player_thanks",category=["misc", "you", "monika"],prompt="Monika...",pool=True,unlocked=True,))


init -990 python:
    store.mas_submod_utils.Submod(
        author="Shinshareddit",
        name="Thanks-moni",
        description="A small submod that allows you to say Thank-you to Monika.",
        version="0.3",
        settings_pane="Submods"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Thanks",
            user_name="ShinshaGitHub",
            repository_name="Thanks-moni"
        )









label player_thanks:
    m 2etd "Yes, Dear~?"
    m 7esb "I'm all ears!"
    menu:
        "Thank you, Monika. For everything.":

            m 5dubfa "..."
            m 3hubsu "Ehehe~"
            m 3hubsb "No problem [player]~"
            menu:
               "I really mean it.":

                    m 5hubfb "Thanks [player], it means alot coming from you~"
                    $ mas_gainAffection(10,bypass=True)
                    jump monika_essp

               "I don't mean it.":
                    m 2dsu "..."
                    jump monika_crud




        "Monika, I really love you!":

            m 6subfa "..."
            jump monika_love


        "Nevermind":

            jump monika_nevermind


label monika_love:
    $ mas_gainAffection(5,bypass=True)
    m 5lsbfa "...."
    m 5hubfb "I love you more [player]-"
    m 5hubfa "<3~"
return

label monika_nevermind:
     m 3ekb "Okie dokie!"
     m 4nub "I love you~"
     $ mas_gainAffection(2,bypass=True)
return "love"


label monika_crud:
     m 2dftpa "..."
     m 1esb "hehe~"
     m 4essdlb "Sorry I couldn't keep it together, heh~"
     m 5hubfa "Don't joke like that again, okay?"
     menu:
        "Okay, I'm sorry monika. I won't ever do it again.":
            m 6hubfb "It's fine [player]. I still love you~"
return "love"


label monika_essp:
    m 5dubfb "I love you [player], don't ever forget that."
return "love"
