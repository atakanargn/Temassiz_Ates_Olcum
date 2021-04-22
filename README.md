# Fakülte Girişleri için Temassız Termometre
Isparta Uygulamalı Bilimler Üniversitesi, Arge ve Inovasyon kulübü yönetimindeyken hazırladığı bir proje. 
Bu projede MLX90614 temassız ateş ölçer cihazını Raspberry Pi ile haberleştirdikten sonra HDMI girişli herhangi bir cihaz ile değerleri yansıttık. Ölçüm yapılmadığı durumlarda ise kamuspotu oynattık.

# Yapılacaklar
#$ sudo nano /boot/config.txt
Belgenin sonuna ekle;
    disable_splash=1

#$ sudo nano /usr/share/plymouth/themes/pix/pix.script
Bu yazılara benzer yerleri sil
    message_sprite = Sprite();
    message_sprite.SetPosition(screen_width * 0.1, screen_height * 0.9, 10000);
    my_image = Image.Text(text, 1, 1, 1);
    message_sprite.SetImage(my_image);

#$ sudo nano /boot/cmdline.txt
    console=tty1 -> console=tty3
    en sonuna;
        splash quiet plymouth.ignore-serial-consoles logo.nologo vt.global_cursor_default=0

#$ sudo reboot

# EKRAN DÖNDÜRME
#$ sudo nano /boot/config.txt
belgenin sonuna;
    display_rotate=0  -> 0
    display_rotate=1  -> 90
    display_rotate=2  -> 180
    display_rotate=3  -> 270