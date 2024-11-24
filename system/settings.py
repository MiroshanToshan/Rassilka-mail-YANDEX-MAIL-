import customtkinter
import json





def config():
    setting =  customtkinter.CTk()

    setting.title("Настройки")

    setting.geometry("450x450") 


    with open("config.json", "r", encoding="UTF-8") as config_js:
        configs = config_js.read()
    configs = json.loads(configs)


    customtkinter.set_appearance_mode("dark") 



    my_name_entry = customtkinter.CTkEntry(setting, placeholder_text=configs["my_name"])
    my_name_entry.place(x=161,y=150)


    my_mail_entry = customtkinter.CTkEntry(setting, placeholder_text=configs["my_mail"])
    my_mail_entry.place(x=161,y=200)


    password_entry = customtkinter.CTkEntry(setting, placeholder_text=configs["password"])
    password_entry.place(x=161,y=250)

    main_label = customtkinter.CTkLabel(setting, text="Настройки", fg_color="transparent", font=('Times 30',35) )
    main_label.place(x=140, y=70)

    my_mail_label = customtkinter.CTkLabel(setting, text="Вашe имя", fg_color="transparent", font=('Times 30',11) )
    my_mail_label.place(x=100, y=150)

    password_label = customtkinter.CTkLabel(setting, text="Ваша почта", fg_color="transparent", font=('Times 30',11) )
    password_label.place(x=95, y=200)

    my_name_label = customtkinter.CTkLabel(setting, text="Ваш пароль", fg_color="transparent", font=('Times 30',11) )
    my_name_label.place(x=95, y=250)








    
    button = customtkinter.CTkButton(setting, text="Сохранить настройки", command=lambda: save_settings(my_mail_entry, password_entry ,my_name_entry, configs, setting))
    button.place(x=161,y=350)
    setting.mainloop()




def save_settings(my_mail_entry, password_entry ,my_name_entry,configs,setting):

    new_settings = {}
    #проверка маймейл
    if my_mail_entry.get() == "":
        new_settings["my_mail"] = configs["my_mail"]
    else:
        new_settings["my_mail"] = my_mail_entry.get()

    #проверка пассворд
    if password_entry.get() == "":
        new_settings["password"] = configs["password"]
    else:
        new_settings["password"] = password_entry.get()

    #проверка майнейма
    if my_name_entry.get() == "":
        new_settings["my_name"] = configs["my_name"]
    else:
        new_settings["my_name"] = my_name_entry.get()


    # new_settings= {
    #     "my_mail" : my_mail_entry.get(),
    #     "password": password_entry.get(),
    #     "my_name" : my_name_entry.get()
    # }

    print(new_settings)
    


    with open('config.json', 'w', encoding='UTF-8') as file:
        json.dump(new_settings, file)
    
    setting.destroy()
    
    
    





   