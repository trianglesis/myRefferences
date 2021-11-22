 # -*- coding: utf-8 -*-

from pynput import mouse, keyboard

keys_options = {
    'Key.cmd': 'Win',
    'Key.alt_l': 'AltL',
    'Key.alt_gr': 'AltR',
    'Key.ctrl_l': 'CtrlL',
    'Key.ctrl_r': 'CtrlR',
    'Key.shift': 'ShiftL',
    'Key.shift_r': 'ShiftR',
    'Key.caps_lock': 'CAPS',
    'Key.enter': 'Enter',
    'Key.backspace': 'Backsp',
    'Key.tab': 'Tab',
    'Key.up': 'Up',
    'Key.left': 'Left',
    'Key.right': 'Right',
    'Key.down': 'Down',
    'Key.insert': 'Ins',
    'Key.home': 'Home',
    'Key.page_up': 'pUp',
    'Key.page_down': 'PDown',
    'Key.delete': 'Del',
    'Key.end': 'End',
    'Key.print_screen': 'PrntSc',
    'Key.scroll_lock': 'ScrLock',
    'Key.num_lock': 'NumLock',
    'Key.pause': 'Pause',
    'Key.esc': 'Esc',
    'Ins': 'Ins',
    'Del': 'Del',
    'Enter': 'Enter',
    'other': '.',
}


def key_press(key):
    f = open('keylogger.txt', 'a', encoding='utf-8')
    k_press = str(key)

    if k_press in keys_options:
        s_note = f'{chr(9650)} {keys_options[k_press]}'
        print(s_note)
        f.write(s_note)
    elif 'Key.' in k_press:
        s_note = f"{chr(9650)} {k_press}"
        print(s_note)
        f.write(s_note)
    else:
        s_note = f"."
        print(s_note)
        f.write(s_note)


def key_release(key):
    f = open('keylogger.txt', 'a', encoding='utf-8')
    k_press = str(key)

    if k_press in keys_options:
        s_note = f'{chr(9660)} {keys_options[k_press]}'
        print(s_note)
        f.write(s_note)
    elif 'Key.' in k_press:
        s_note = f"{chr(9660)} {k_press}"
        print(s_note)
        f.write(s_note)
    else:
        s_note = f"."
        print(s_note)
        f.write(s_note)


with keyboard.Listener(on_press=key_press, on_release=key_release) as key_listen:
    key_listen.join()


