import view
import model
import text_fields as txt

def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_successful)  
            case 2:
                model.save_file
                view.print_info(txt.save_successful)
            case 3:
                pb =  model.load_file()
                view.show_contacts(pb, txt.no_contact_or_file)
            case 4:
                contact= view.new_contact()
                model.add_contact(contact)
                view.print_info(txt.new_contact_successful)
            case 5:
                name = view.find()
                result = model.find_contact(name)
                view.show_contacts(result, txt.not_find(name))
            case 6:
                ph = model.phone_book()
                view.show_contacts(pb, txt.empty_or_not_open_file)
                if pb:
                    change_contact= view.change_contact(pb, txt.input_index)
                    model.change_contact(change_contact)
                view.print_message(txt.change_successful(change_contact[1].get('name')))
            case 7:
                ph=model.get_pb()
                view.show_contacts(pb, txt.empty_or_not_open_file)
                if pb:
                    index = view.input_index(pb, txt.delete_index)
                    if view.confirm(txt.confirm_delete(pb[index-1].get('name'))):
                        view.print_massege(txt.del_contact(model.delete_contact(index)))
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_changed):
                        model.save_file()
                view.print_info(txt.bye_bye)
                exit()
            
            