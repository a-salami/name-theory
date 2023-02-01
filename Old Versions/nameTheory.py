#pyinstaller  --onefile  nameTheory.py: for re-creating the executable
print("- Welcome to Allison's Name Theory! -"
    "\nEntering a name will give you an idea of what kind of personality that name will have, based on first letter and/or full name."
    "\nIf your person's name has a trend, you may get advice specific to them. If there is no specific advice for your name, general rules of thumb for their letter will be presented to you."
    "\n\nPlease note that inputting your nickname may get you a different result than your full first name. Try them all!\n")

firstName = str(input("What is their name? ")).capitalize()

while firstName != "Done":
    gender = str(input("And what is their gender (M or F)? ")).capitalize()
    majorityAdvice = False
    print("")

    #gives specific advice based on the name, not just the first letter
    if firstName[0] == 'A':
        if firstName == 'Aaron':
            print("Aarons are completely untrustworthy. They are, frankly, bad at covering it up, but they have a way of making you overlook things."
            "\nIf you're not careful, you will stop seeing the red flags and start making excuses for them. Don't go there.")
        elif firstName == "Alexis":
            print("Alexises are liked by pretty much everyone, and for good reason. They're outgoing and comfortable in social situations, and they know how to keep a crowd engaged."
            "\nThey're not necessarily the best at reading the room, so keep that in mind, whatever that may mean for your situation with her (social/dating/etc.)")
        elif firstName == 'Alia':
            print("Please do yourself a favor and do not, under any circumstances, get close."
            "\nShe likely seems innocent enough on the outside, but she'll very quickly draw you into her mess and coerce you into 'helping' her."
            "\nIf you're too kindhearted to say no, help from afar. If you're not, disengage right away and thank me later."
            "\nShe's a drama queen of obscene proportions. Don't let her fool you. She may mean well, but she will drag you into a state of no longer meaning well quite easily. Be careful.")
        elif firstName in {'Allison', 'Allyson', 'Alison', 'Alyson', 'Alisyn', 'Alysyn', 'Allisyn', 'Allysyn'}:
            print("A(l/ll)(i/y)s(o/y)ns are a 50-50 split. She's either annoying or quiet, but neither are to a high degree."
            "\nIf she's an annoying one, it's not so incredibly annoying that you can't stand her. You'll probably end up being friends, too."
            "\nIf she's a quiet one, she's not painfully introverted, but don't be surprised if you have to make the first move if you want to talk to her.")
        elif firstName in {'Alyana', 'Aliyana', 'Aliana'}:
            print(firstName + "s can be kind of rough to deal with."
            "\nShe'll do anything to get what she wants, and will propably manipulate you into helping her."
            "\n" + firstName + "s also tend to be drama queens. If you're not into that, then watch your back.")
        elif firstName == 'Amanda':
            print("Amandas are hardheaded and stubborn, but you will love them."
            "\nThey're hilariously funny, whether you share their direct sense of humor or not."
            "\nYou'll need to be patient with your Amanda- that aforementioned stubbornness can get in the way of your relationship if you let it. Work through it and you'll be golden.")
        elif firstName == 'Andrew':
            print("Treasure your Andrew for all eternity. He's an absolute joy to have as a friend. Keep him close and you will be glad you did."
            "\nThey tend to be introverted, so you may have to approach him first, but once you establish mutual trust, be patient (do not push it) and he will open up to you."
            "\nThere's hardly an Andrew out there not worth putting time and emotion into. Keep him safe.")
        else:
            majorityAdvice = True

    if firstName[0] == 'B':
        if firstName == 'Bobby':
            print("Moreso than their Robert counterparts, Bobbys are slightly childish. They are likely holding onto some things from their formative years, including their nickame."
            "\nThink about it- does any Robert in a professional setting go by Bobby? By the time they get to the workplace, Bobbys have shed their former nicknames and embraced a more mature self.")
        else:
            majorityAdvice = True
    
    if firstName[0] == 'C':
        if firstName == 'Caleb':
            print("Your Caleb is crazy, period, but in-a-good-way crazy. They have an endearing personality and a lovely spirit. You'll want to know him, and you should!"
            "\nThey just enjoy putting themselves in danger by doing things that you would call reckless and they would call fun."
            "\nThey are pure adrenaline junkies.")
        elif firstName in {"Chris", "Christian"}:
            print("Be prepared to be in for the long haul if you want to really know your Chris. They're laid-back to a fault, so much so that you'll rarely know their true personality."
            "\nThey're not at all confrontational and drama repels them, but that can work against you if you are waiting for them to express their feelings. They're not very emotionally expressive."
            "\nBe patient with him. He needs time to get comfortable with you.")
        elif firstName in {'Connor', 'Conner'}:
            print(firstName + "s are very impressionable, and they're easily led by others. They don't have a strong sense of self, and the people who they engage with will heavily influence who they become."
            "\nChoose your " + firstName + " carefully; he needs time to grow up.")
        else:
            majorityAdvice = True
    
    if firstName[0] == 'D':

        if firstName == 'Dan':
            print("Your Dan may strike you as hard to approach at first. He seems a little serious and academic, perhaps, in a way that says 'don't approach me'. But do approach him!."
            "\nDans aren't the easiest people to get to know, but once you do, you'll open up a world of conversation and the potential for a lifelong relationship with them.")
        elif firstName == 'Danny':
            print("Danny, your sweet, precious Danny. He's going to be childish for a little longer than everyone else, but he's largely high-spirited and fun to have around."
            "\nHe's likely emotionally driven and can be quick to switch between the highs of different feelings. Be mindful of that- a stray comment you think nothing of might affect your Danny more than you anticipate.")
        elif firstName == 'Daniel':
            print("Your Daniel can be a little stoic sometimes. He has a great sense of humor and is personable enough, but if you were to look over at him when his face is in a resting state, you may be intimidated."
            "\nDon't let that indimidate you. Daniels are sweethearts who have the time of day for anyone who asks.")
        elif firstName == 'Danielle':
            print("Danielles are very outgoing and outspoken; they thrive in social settings. They love sharing their thoughts and time with others."
            "\nAt first blush, she may seem spacey or forgetful, but don't let that cement your opinion of her. She's intelligent, and especially knowledgeble in things she cares about.")
        elif firstName == 'David':
            print("It's 'my way or the high way' with Davids. You have to leave them alone in terms of letting them grow up- they will not learn by someone telling them what to watch out for."
            "\nThey thrive on personal experience and will only wish to do the things you tell them not to do. Push them too far and they will lash out, whether emotionally or physically. Give them space to thrive and they'll come back down.")
        elif firstName == 'Donovan':
            print("Donovans are crazy. Fair warning, you will not know that until you stop knowing them. Be careful."
            "\nThey're lovable and well-loved, and it's likely that the people closest to him are just as enamored as you were.")
        else:
            majorityAdvice = True
    
    if firstName[0] == 'E':

        if firstName == 'Ellie':
            print("Ellies are awesome. They're easy to talk to and great at carrying enjoyable conversations. Ellies make you feel at home in situations where you normally wouldn't.")
        elif firstName == "Emma":
            print("Emmas are laid-back and easygoing, but don't try to force a friendship. She'll open up to you when she feels as if you've earned it, so don't expect deep conversations off the bat."
            "\nIf you're in a relaxed social setting, she's a great part of the conversation. Her humor is usually an undercurrent of her communication- she'll keep you laughing with consistant, deadpan jokes.")
        else:
            majorityAdvice = True

    if firstName[0] == 'J':

        if firstName == 'James':
            print("James is a perpetual clown and he knows it. He lives for it. His soul purpose for a long time will be to egg people on and serve as the life of the party.")
        elif firstName == 'Jay':
            print("Whether their name is actually Jay or they go by Jay, boy or girl, cease and desist ASAP. You're welcome.")
        elif firstName == 'Jenna':
            print("Jennas are loveable oddballs. They don't like direct attention but they do enjoy standing, typically when it comes to appearance."
            "\nThey're great friends to have and they'll have you laughing within the first few minutes of conversation. Get to know your Jenna and you'll have true friend for whatever season of life you're in.")
        elif firstName[0:4] == 'Josh':
            print("Your Josh has a 50-50 shot of either being great or kind of the worst. They are usually sweet enough, on an acquaintance level."
            "\nGet any closer, and you may find yourself dealing with more than you bargained for.")
        elif firstName == 'Jacob':
            print("A Jacob. Good heavens, and good luck to you (I'm only exaggerating a little bit)."
            "\nJacobs are usually kindhearted, but that kindheartedness might be buried under layers of another, more negative personality trait or habit."
            "\nThat negative trait or habit usually can be overlooked, but not very easily. You'll have to work with your Jacob, but their kindheartedness might make it easier and worth your while.")
        elif firstName == 'Joe' or 'Joseph' or 'Jerry' or 'Jeremiah' or 'Josiah':
            print("A " + firstName + "! " + firstName + "s are usually pretty cool. They most assuredly have some odd quirks, but they're lovable and nice to have around."
            "\nUnlike most other Js, getting close to a " + firstName + " will likely do you much more good than harm.")
        elif firstName == "Joel":
            print("Joels are extroverted and funny, and they're a blast to have around."
            "\nIt's likely that you'll never get really close with a Joel one-on-one, but he'll always be around in group settings."
            "\nJoels tend to be talented, one of those good-at-everything people, but they're not conceited about it. They will joke as if they are, but they're sweethearts about their skill."
            "\nKeep your Joel around. He's probably really cool.")
        elif firstName == 'John':
            print("Johns are dangerous. You're not supposed to like them, but you most often will. As long as you don't get too close, you've got a good setting-friend (eg. school-friend / work-friend)."
            "\nWord to the wise- never try to change a John. They're set in their ways and if they're going to change, it'll be on their time and their dime. They will not change for or because of you.")
        else:
            majorityAdvice = True
  
    if firstName[0] == 'K':

        if firstName in {'Katie', 'Katy'}:
            print("You probably grew up with a " + firstName + " and she was probably a little wild. The way that your " + firstName + " is largely dependent on whether you grew up with her."
            "\nIf you grew up with her, she might act differently toward you becaue of the history between you two. Perhaps you elevate the wildness in her, or maybe you tone it down."
            "\nIf you didn't grow up with her, she'll likely be wild out the gate. You'll have to set your boundaries quickly in order to establish a lasting relationship.")
        elif firstName == "Kenny":
            print("If your Kenny goes by Kenny, it's because he wants to embrace extrovertedness. He donned the Kenny personality to make that transition easier."
            "\nIf your Kenny is one by birth, he's probably all-in on his extrovertedness. He doesn't necessarily have to embrace it like a Kenny-nickname will. He's born with it (he's Maybelline).")
        elif firstName in {'Kenneth', 'Kai'}:
            print(firstName + "s are subdued and extremely introverted- perhaps painfully so. You will not know a " + firstName + " unless he wants you to know him.")
        elif firstName == 'Kevin':
            print("Kevins grow up to take one of two paths. They all start out as lovable but weird little kids."
            "\nThey will either grow up in that weirdness until it makes them an offputting adult, or they seriously mellow out and end up being rather cool.")
        else:
            majorityAdvice = True

    if firstName[0] == 'M':

        if firstName == 'Madison':
            print("Your Madison is most likely pretty relaxed. She's not necessarily introverted, but she's quiet, and likely prefers to observe before speaking."
            "\nShe probably has a few close friends with whom she is more relaxed; approach her while she's with them if you want the full effect of your Madison.")
        elif firstName in {'Maddie', 'Maddy', 'Mady'}:
            print("You've got a sweetheart. Your " + firstName + " may be a little spacey and might not be the most observant girl on the planet, but she's a loyal friend and a ton of fun.")
        elif firstName in {'Max', 'Maxwell', "Maximillion"}:
            print("Maxes are hard to know and hard to get to know. They tend to keep to themselves and are very good at floating on the waters of menial conversation."
            "They're generally agreeable, though, so take your time with them.")
        elif firstName == 'Michael':
            print("You have a 50-50 shot with your Michael: either the two of you click right away or clash hard. There's usually no in between."
            "\nIf you both click, then you'll most likely end up with an setting-based relationship (eg. work-friend or school-friend). He will be your buddy through and through."
            "\nIf you both clash, do not fret, all is not lost. You will have to smooth out the bumps in your dynamic, but once you do, work from there. Work hard and the relationship will prosper.")
        else:
            majorityAdvice = True

    if firstName[0] == 'N':

        if firstName == 'Natasha':
            print("Lucky you! Natashas are wonderful and lovely, even if they might be little strange."
            "\nTreasure your Natasha dearly- they are absolute gems.")
        elif firstName == 'Nathan':
            print("It's hard to know a Nathan. He doesn't wear his heart on his sleeve and he won't open up to you immediately."
            "\nGive him time- he'll come around and you'll be amiable in no time.")
        elif firstName == 'Nicholas':
            print("Nicholases are stubborn, and that is their shining, defining trait. If he introduces himself as Nicholas to you, you'll likely never get to call him Nick."
            "\nHe's set in his ways and is comfortable there. Try not to upheave him too much.")
        elif firstName == 'Nick':
            print("Nicks are dangerous. You're not supposed to like them, but you most often will. Make sure you are always aware of who you're dealing with when pouring time into a Nick."
            "\nThat's not to say you shouldn't get close to a Nick. Just be mindful, because if you are, you could end up with a truly spectacular friend."
            "\nWord to the wise- don't try to change your Nick. He's set in his ways and if he's going to change, it'll be on his time and his dime. He will not change for or because of you.")
        elif firstName == "Nico":
            print("Nico will be one of two things as he grows up: playful or emo. He'll always grow out of the emo, but never out of the playful.")
        else:
            majorityAdvice = True

    if firstName[0] == 'O':

        if firstName in {'Olive', 'Olivia'}:
            print("Be careful; " + firstName + "s are especially wild.\nAn Olive would be the kid in your group who was a biter, and ran around with scissors because she knew it scared people and she liked that.")
        elif firstName == 'Opal':
            print("Run. Opal is absolutely out of her mind. \nIf an Olive or Olivia is crazy, an Opal is three tiers above her. Olive liked to run with scissors, Opal liked to stab people with them.")
        else:
            majorityAdvice = True

    if firstName[0] == 'R':
        if firstName == 'Robert':
            print("Roberts aren't inherently bad or ill-meaning people, but they are inherently flaky."
            "You might want to avoid serious relationships with them until they've done some serious introspection and growing up.")
        elif firstName == 'Ryan' and gender == 'F':
            print("Everybody is going to like your Ryan and it's going to annoy you. She's likely popular and everyone wants to be her friend."
            "\nIf you two grew up together, you may drift apart if she isn't as keen on you as you are on her. The popularity likely will get to her head a bit."
            "\nDon't give up on her, though. She'll come back around.")
        elif firstName == 'Ryan' and gender == 'M':
            print("Ryans are perpetually cocky, whether they let you know it or not."
            "\nIf he's an extrovert, he likely jokingly pretend to be cocky to distract from actual cockiness and he believes he has everyone fooled."
            "\nIf he's an introvert, he likely believes he's better than other people at a lot of things. He doesn't necessarily think he's a better person, though."
            "\nEither way, your Ryan's a good person. He may be cocky, but it could be for good reason. Even if it isn't, love on your Ryan anyway. He's good to have around.")
        else:
            majorityAdvice = True
    
    if firstName[0] == 'S':

        if firstName in {'Sofi', 'Sophi'}:
            print("Wild. She's up there with the most wild girls there are. She probably knows or used to know an Olive or Opal, and they probably got along great because they're all very similar."
            "\nHowever, you're in luck. While your " + firstName + " is wild, she's not crazy. You'll have a hard time reigning her in, but she's highly entertaining to have around.")
        elif firstName in {'Sofia', 'Sophia'}:
            print("Ah, " + firstName + "s are usually party animals. They're a litle wild and tend to develop a 'dgaf', carefree attitude toward toward life."
            "It's likely that she'll mellow out in the future, especially if you knew her as a kid and she was mellow then.")
        elif firstName[0:3] == 'Sam':
            print("Sams are always pretty cool, particularly if they go by 'Sam' as a nickname."
            "\nYou really can't go wrong with a Sam. Heads up- if you want one to open up to you, you'll need to work at it."
            "\nThey tend to be introverted, but they come off as extroverts and they play that role well. They aren't so great at sharing their emotions. Be patient with them.")
        else:
            majorityAdvice = True

    if firstName[0] == 'V':
        if gender == 'F':
            print("V girls are an interesting bunch. They have the highest propensity for evil out of all other girl names."
            "\nNote that this doesn't mean your V will be evil, but Vs are simply more likely to be evil than any other girls. And if she is evil, you will see it."
            "\nIf she does not rise to the occasion of being evil, then she will end up being a rather peaceful girl."
            "\nYou are probably either friends with a V girl now or you knew one when you were a kid, and she was probably alright."
            "\nDespite the aforementioned propensity, they make good friends, as long as they don't rise to that evil.")

        if firstName in {'Vanessa', 'Violet'}:
            print("\nNow here, you have an exception. Your " + firstName + " is a V, and she still does have that propsensity for evil."
            "\nHowever, she does have the lowest possible propensity out of all the other V girls to rise to that evil."
            "\nAnd if she doesn't rise to it, she may fall into the trap of becoming harmless, whereas the rest of the Vs will likely become peaceful.")
        else:
            majorityAdvice = True

    if firstName[0] == 'W':
        
        if firstName[0:4] == "Will":
            print(firstName + "s are great! You can't really go wrong. They tend to be social introverts- they can hold a conversation but won't necessarily look to start one."
            "\nThey're solid friends and good folk to have around.")
        else:
            majorityAdvice = True

    if firstName[0] == 'T':
        if firstName == "Tiffany":
            print("Tiffanys will likely annoy you. They might come across as shallow due to their desire to be liked."
            "\nThey crave attention and others' validation, so keep that in mind when approaching."
            "\nYou can have a good relationship with a Tiffany as long as you keep this in mind.")
        elif firstName == "Tyler":
            print("Tyler is going to annoy the crap out of you, but you're going to love every second you spend with them."
            "\nYou're going to wonder why you're friends with them and what you'd do without them on a daily basis, simultaneously."
            "\nTylers can be blast to have around, all in all. They pick up on humor and dynamic quickly, and once they do, it's all over- you're stuck with a great friend.")
        else:
            majorityAdvice = True
    
    if firstName[0] == 'Z':
        if gender == 'M':
            print("You probably won't hear much from a Z guy. He's most likely pretty reserved, and won't say much.\n")
        elif gender == 'F':
            print("Your Z girl is probably a little haughty, and she might think she's better than everyone else."
            "\nDon't let that totally deter you- she's pretty cool once you get to know her, but she is a little self-centered.")

        if firstName[0:3] in {'Zac', 'Zak'}:
            print("Except " + firstName + "s aren't actually quiet. At all."
            "\n" + firstName +"s tend to be loud and proud of it. They tend to be your typical jocks on the surface, but most likely have a few more intellectual levels to them, too."
            "\nTake your time with your " + firstName + ". There's probably more depth to him than you realize.")
        else:
            majorityAdvice = True

    #checks if the user wants to see the majority advice, only if they entered a specific name
    if majorityAdvice == False:
        print("\n---------------------------------------------------------------------------------------------------------------------")
        majorityAnswer = str(input("\nBecause you entered a name that warranted specific advice, you are seeing what is applicable to them as opposed to advice that applies to the majority of that letter."
        "\nWould you like to see the majority advice? Type yes or no: ")).capitalize()

        if majorityAnswer in {'Yes', 'Y'}:
            majorityAdvice = True
        else:
            print("~majority advice skipped")

    #gives the majority advice based on the name's first letter
    if majorityAdvice == True:
        print("\n- Majority Advice: " + firstName[0] + " -\n")

        if firstName[0] == 'A':
            print("Overall, quite an interesting bunch. Many A names are a bit crazy and a little strange, but in an oddly endearing way. They're great friends once you get to know them."
            "\nThey usually hold a few traits that seem a little 'much' to handle or are simply annoying, but they are typically easy to look past."
            "\nIf you're willing to get to know an A on a deeper level, they're cool to hang around.")
        elif firstName[0] == 'B':
            print("--")
        elif firstName[0] == 'C':
            print("--")
        elif firstName[0] == 'D':
            print("--")
        elif firstName[0] == 'E':
            print("--")
        elif firstName[0] == 'F':
            print("--")
        elif firstName[0] == 'G':
            print("--")
        elif firstName[0] == 'H':
            print("--")
        elif firstName[0] == 'I':
            print("--")
        elif firstName[0] == 'J':
            print("Word to the wise- be mindful."
            "\nJs can present trouble. Upon first impression, they seem perfectly friendly."
            "\nThe more you get to know them, the more obvious it will become that they have some negative traits that can't be overlooked."
            "\nMany Js are manipulative, but you won't realize you're being manipulated until after you've ended the relationship with them."
            "\n\nOn the bright side, Js are pretty funny, or often do funny/stupid things that you can chuckle about later."
            "\nJs are fine, if you don't get too close. And if you do, just know who you're dealing with.")
        elif firstName[0] == 'K':
            print("Your K is probably pretty chill. They tend to have a go-with-the-flow outlook on life, and are not easily stressed by abrupt change."
            "\nIf you want to go on a spontaneous adventure, a K might be a good person to take with you.")
        elif firstName[0] == 'L':
            print("--")
        elif firstName[0] == 'M':
            print("--")
        elif firstName[0] == 'N':
            print("N names are usually fun, approachable, and ambiverted."
            "\nYou might have to approach them first, but you'll be glad you did. They make solid friends and are easy to talk to."
            "\nNs are usually pretty loyal, too, so don't worry about them talking behind your back. Keep one near to you and you'll be glad you did.")
        elif firstName[0] == 'O':
            print("The personality of an O is dependent on their gender."
            "\nIf your O is a girl, she's crazy. If he's a boy, you're more likely to meet a pretty mellow guy.")
        elif firstName[0] == 'P':
            print("--")
        elif firstName[0] == 'Q':
            print("--")
        elif firstName[0] == 'R':
            print("--")
        elif firstName[0] == 'S':
            print("S-s are fun to hang around. They're usually down for a good time."
            "\nThey may take a minute to open up, but once they do, you have a solid friend and person to be around.")
        elif firstName[0] == 'T':
            print("--")
        elif firstName[0] == 'U':
            print("--")
        elif firstName[0] == 'V':
            print("\nV-s as a whole are usually pretty cool, but they are more inclined to be chill if they are male."
            "\nV girls do have a higher likelihood for evil than other girls, but if they don't fall into that, they're just as cool as the guys."
            "\nWatch them close- if you see things you don't like, keep your distance. If they seem fine, they probably are, and they're great friends to have!")
        elif firstName[0] == 'W':
            print("--")
        elif firstName[0] == 'X':
            print("--")
        elif firstName[0] == 'Y':
            print("--")
        elif firstName[0] == 'Z':
            print("The personality of a Z is dependent on their gender."
            "\nIf your Z is a boy, he's usually quiet, and lays low in conversation."
            "\nGirl Zs are a little more extroverted, enjoy having others' attention, and tend to be conceited. They know (and slightly overestimate) their worth and will not hide that.")

    print("\n---------------------------------------------------------------------------------------------------------------------")
    firstName = str(input("\nIf you're done, type 'done' and this window will close. If you'd like to enter another name, type it here: ")).capitalize()
