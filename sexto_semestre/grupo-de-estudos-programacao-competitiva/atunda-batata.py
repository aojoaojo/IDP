while True:
    try:
        parte = input()
        if 'E lindo dizer!' in parte:
            print('suricato', flush=True)
        elif 'Sim, vai entender!' in parte:
            print('facochero', flush=True)
        elif 'Os seus problemas voce deve esquecer!' in parte:
            print('leao', flush=True)
        else:
            continue

    except EOFError:
        break