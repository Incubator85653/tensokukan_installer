A super simple naive installer framework written in Python 3.
=============================================================
Perhaps you will glad to call it "SSN setup".

Like other common installer frameworks, SSN design for grab information from the user and unpack program files for them automatically.

Features
--------
- Unpack 7-zip archives to a user specified path.
- Multiple language support.
- Modify installed config files as needed.
- Create shortcuts on the desktop and start menu.
- Upgrade exist program.
- Modular installer step writing experience (1)

(1): Have you heard about "The Elder Scroll: Skyrim" or "Garry's Mod"? The SSN doesn't care how many steps it would have. It runs every available step from the list. Just like add a mod to the game.

Frequently asked questions
--------------------------
**There're lots of great installer frameworks all around the world, like Inno and InstallShield, why are you start this project?**

- The answer is quite simple. I'm looking for an easy way to install a software called "Tensokukan" for my friends(too many people of them). 
Tensokukan, it does not provide an installer. So unpack the files and do settings configure became a big problem.

  Unfortunately, because of my IQ, it's hard to figure out how to use those installer frameworks(Wix, Inno, etc). So I write a framework for myself. A super simple, easy to use installer, for those people who are naive and fools(for example, me).

**Should I use SSN for my program? What case, and Why?**
- SSN is a very tiny installer framework. It can't provide many important features if you're writing business and engineering code.
  I'm pretty sure you never want to use it in USA Air force software project.
  Things you should know...
  
- SSN can't do:
  - Version management
  - Previous step button (1)
  - Implement an installer without modifying SSN source code (2)

  (1): Yes you can't back to the previous step after click next step, on future update SSN can back to first step but maybe never implement prev step. This is all the "Modular"'s fail. SSN don't even know what step just activated. It can only restart entire installer from the first step.

  (2): Essentially, SSN is a suite of 7-zip unpack command generator and config file editor. But it's easy to plugin yourself feature and code into SSN. So if you want something, you implement it yourself.
  
- Then Why I'm going to use it?
  - There're many tiny programs in this world. Many of them have very simple feature and few program files. The fact is a program can't put all the arguments or variables in the source code. Thus config file was born. If you got an "unbound" installed, you will notice that unbound not come with a config editor GUI. Our user just wants very simple feature, configure every time is not a happy thing to do.
  
    SSN is for those tiny programs who want provide out-of-box experience to the user. **I am not saying that unbound is a tiny program.**
