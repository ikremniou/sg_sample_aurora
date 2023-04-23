label main_menu:
    jump start

label start:
    $ sg_aurora.addPostBy("bella", "Freedom.", "ph", 478)
    call screen sg_aurora()
    "Jumping at the beginning. New post is added"
    jump start
