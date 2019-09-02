import sys, os, time, random
from platform import system as detect
b = '\x1b[31;1m'
p = '\x1b[37;1m'
k = '\x1b[33;1m'
c = '\x1b[36;1m'
r = b

class colorku:

    def warning(self, text):
        print p + '+' + b + ('=').center(66, '=') + p + '+'
        print b + '|' + p + (k + text + p).center(80, '-') + b + '|'
        print p + '+' + b + ('=').center(66, '=') + p + '+'

    def out(self, text):
        print p + '+' + b + ('=').center(66, '=') + p + '+'
        print b + '|' + p + (c + text + p).center(80, '-') + b + '|'
        print p + '+' + b + ('=').center(66, '=') + p + '+'

    def warn(self, text):
        print b + '|' + p + (k + text + p).center(80, '-') + b + '|'

    def printf(self, text):
        print b + '|' + p + text.center(66) + b + '|'


cl = colorku()
try:
    from bs4 import BeautifulSoup as ardi
    import requests
except Exception as e:
    cl.warning(' Error : ' + str(e) + ' ')
    sys.exit()
else:
    gagal = '\n    .d8888b.                                         888 888 888\n   d88P  Y88b                                        888 888 888\n   Y88b.                                             888 888 888\n    "Y888b.    .d88b.  888d888 888d888 888  888      888 888 888\n       "Y88b. d88""88b 888P"   888P"   888  888      888 888 888\n         "888 888  888 888     888     888  888      Y8P Y8P Y8P\n   Y88b  d88P Y88..88P 888     888     Y88b 888       "   "   "\n    "Y8888P"   "Y88P"  888     888      "Y88888      888 888 888\n                                            888\n                                       Y8b d88P\n                                        "Y88P" '

    def banner():
        print p + '+' + b + ('=').center(66, '=') + p + '+'
        print b + '|' + p + (' Bot Create SSH SSL ').center(66, '-') + b + '|'
        print b + '|' + p + ('-').center(66, '-') + b + '|'
        print b + '|' + p + (' Penyedia SSH : http://www.jetssh.com ').center(66, '-') + b + '|'
        print b + '|' + p + ('-').center(66, '-') + b + '|'
        print b + '|' + p + (' Coded By Mr.A_S ').center(66, '-') + b + '|'
        print p + '+' + b + ('=').center(66, '=') + p + '+'
        print


    def ssh7():
        global a
        data = {1: [
             'Asia',
             {1: [
                  'Singapore', 'http://www.jetssh.com/ssh-server-sg'],
                2: [
                  'India', 'http://www.jetssh.com/ssh-server-in']}],
           2: [
             'Amerika',
             {1: [
                  'United States', 'http://www.jetssh.com/ssh-server-us'],
                2: [
                  'Canada', 'http://www.jetssh.com/ssh-server-ca']}],
           3: [
             'Europe',
             {1: [
                  'Germany', 'http://www.jetssh.com/ssh-server-de'],
                2: [
                  'Netherland', 'http://www.jetssh.com/ssh-server-nl'],
                3: [
                  'United Kingdom', 'http://www.jetssh.com/ssh-server-uk']}]}
        while True:
            os.system('clear')
            banner()
            print ('[+] SSH 7 Hari [+]').center(68)
            print '\n  [+] Pilih Salah Satu Server :\n'
            for no, (asia, datas) in data.items():
                print ('      {0}). {1}').format(no, asia)

            try:
                print
                ops = int(raw_input('  [+] Masukkan Nomor : '))
                break
            except ValueError:
                print
                cl.warning(' PILIH PILIHAN YANG SUDAH ADA ')
            except KeyError:
                print
                cl.warning((' NOMOR {} TIDAK ADA, ANDA MUNGKIN BUTA ').format(ops))
            else:
                time.sleep(1)
                continue

        while True:
            os.system('clear')
            banner()
            print ('[+] SSH 7 Hari [+]    [+] ' + data[ops][0] + ' [+]').center(68)
            print '\n  [+] Pilih Salah Satu Negara :\n'
            for no, (nom, nomb) in data[ops][1].items():
                print ('      {0}). {1}').format(str(no), nom)

            try:
                print
                opa = int(raw_input('  [+] Masukkan Nomor : '))
                break
            except ValueError:
                print
                cl.warning(' PILIH PILIHAN YANG SUDAH ADA ')
            except KeyError:
                cl.warning((' NOMOR {} TIDAK ADA, ANDA MUNGKIN BUTA ').format(opa))
            else:
                time.sleep(1)
                continue

        a = '[+] SSH 7 Hari [+]    [+] ' + data[ops][0] + ' [+]' + '   [+] ' + data[ops][1][opa][0] + ' [+]'
        return [
         data[ops][1][opa][1], 'http://www.jetssh.com/create-account-ssh-3-days.php', 'SSH']


    def main():
        global a
        data = {2: ['http://www.jetssh.com/ssh-server-sgdo', 'http://www.jetssh.com/create-account-ssh-3-days.php', 'SSH'], 3: [
             'http://www.jetssh.com/ssl-server', 'http://www.jetssh.com/create-account-ssl.php', 'SSL']}
        while True:
            os.system('clear')
            banner()
            print '  [+] Pilih Salah Satu : \n'
            print '      1). SSH 7 Hari'
            print '      2). SSH Server SGDO 7 Hari'
            print '      3). SSH SSL 30 Hari'
            print '      0). Keluar\n'
            try:
                cmd = int(raw_input('  [+] Pilih yang mana : '))
                print
            except ValueError:
                print
                cl.warning(' PILIH PILIHAN YANG SUDAH ADA ')
                time.sleep(1)
                continue
            except KeyError:
                print
                cl.warning((' NOMOR {} TIDAK ADA, ANDA MUNGKIN BUTA ').format(cmd))
                time.sleep(1)
                continue
            else:
                if cmd == 1:
                    ssh = ssh7()
                    return ssh
                if cmd in (2, 3):
                    os.system('clear')
                    banner()
                    if cmd == 2:
                        a = '[+] SSH SGDO 7 Hari [+]'
                    else:
                        a = '[+] SSH SSL 30 Hari [+]'
                    print
                    return [data[cmd][0], data[cmd][1], data[cmd][2]]
                if cmd == 0:
                    cl.out(' Thanks Sudah Menggunakan Tools Saya ^_< ')
                    sys.exit()
                else:
                    cl.warning((' NOMOR {} TIDAK ADA, ANDA MUNGKIN BUTA ').format(cmd))
                    time.sleep(1)
                break


    def mytun():
        try:
            links = requests.get(men[0]).text
            parser = ardi(links, 'html.parser')
            row = parser.find('div', {'class': 'row nomargin'})
            linkss = [ urls['href'] for urls in row.findAll('a') ]
            return linkss
        except requests.exceptions.Timeout:
            cl.warning(' CONNECTION TIME OUT ')
            sys.exit(0)
        except requests.exceptions.ConnectionError:
            cl.warning(' CONNECTION ERROR ')
            sys.exit(0)
        except:
            cl.warning(' SERVER CLOSED TRY ANOTHER SERVER ')
            sys.exit(0)


    def start():
        count = 0
        while True:
            os.system('clear')
            banner()
            print a.center(68)
            print
            name = raw_input('  [+] Masukkan Username : ')
            if len(name) < 4:
                print
                cl.warning(' Password Minimal 4 huruf ')
                time.sleep(1)
                continue
            pwd = raw_input('  [+] Masukkan Password : ')
            out = raw_input('  [+] Masukkan  Output  : ')
            break

        print
        for link in mytun():
            header = {'Origin': 'http://www.jetssh.com', 'Referer': link}
            print p + '+' + b + ('=').center(66, '=') + p + '+'
            try:
                sesi = requests.session()
                req = sesi.get(link)
                serverid = ardi(req.text, 'html.parser').find('input', {'name': 'serverid'})['value']
                param = {'serverid': serverid, 'username': name, 'password': pwd}
                res = sesi.post(men[1], data=param, headers=header, timeout=30)
                hsl = ardi(res.text, 'html.parser')
                sis = [ str(i).replace('<br/>', '').replace('<b>', '').replace('</b>', '') for i in hsl.contents ]
                if len(hsl) >= 10:
                    del sis[1]
                    del sis[1]
                    del sis[2]
                    del sis[3]
                    del sis[4]
                    del sis[5]
                    del sis[6]
                    del sis[7]
                    if men[2] == 'SSH':
                        port = '   OpenSSH Port  : 22\n   Dropbear Port : 80,443'
                    else:
                        port = '   SSL Port  : 443\n   OpenSSH Port  : 22\n   Dropbear Port : 80,3128'
                    lamp = sis[0].center(68) + '\n\n   ' + sis[1] + '\n\n   ' + sis[2] + '\n   ' + sis[3] + '\n' + port + '\n   ' + sis[4] + '\n   ' + sis[5] + '\n\n  ' + sis[6]
                    print lamp
                    file_save(out, p + '+' + b + '=' * 66 + p + '+\n' + lamp + '\n')
                    count += 1
                else:
                    print b + '|' + p + hsl.text.center(66) + b + '|'
            except requests.exceptions.Timeout:
                cl.warn(' CONNECTION TIMEOUT ')
            except requests.exceptions.ConnectionError:
                cl.warn(' CONNECTION ERROR ')

        print p + '+' + b + ('=').center(66, '=') + p + '+'
        print p + '+' + b + ('=').center(66, '=') + p + '+'
        print b + '|' + p + (b + ' ' + str(count) + p + ' Account SSH/SSL Tersimpan Di ' + b + ': ' + p + out + p + ' ').center(101, '-') + b + '|'
        print p + '+' + b + ('=').center(66, '=') + p + '+'
        try:
            with open('/sdcard/Android/data/com.termux/.jet1', 'a+') as (line):
                line.write('1,')
        except:
            os.mkdir('/sdcard/Android/data/com.termux')
            with open('/sdcard/Android/data/com.termux/.jet1', 'a+') as (line):
                line.write('1,')


    def file_save(f, isi):
        if f == '':
            if detect() == 'Windows':
                f = 'c://SSHLog.txt'
            else:
                f = 'SSHLog.txt'
        try:
            with open(f, 'a+') as (files):
                files.write(isi)
        except:
            print
            cl.warning(' KESALAHAN DALAM SAVE FILES ')


    def loading(text):
        num = 0
        while num < 1:
            for i, char in enumerate(text):
                if i == 0:
                    print '\r' + '                  ' + '%s%s%s%s' % (p, char.upper(), r, text[1:]),
                    sys.stdout.flush()
                elif i == 1:
                    old_text = text[0].lower()
                    print '\r' + '                  ' + '%s%s%s%s%s%s' % (r, old_text, p, char.upper(), r, text[2:]),
                    sys.stdout.flush()
                elif i == i:
                    old_text = text[0:i].lower()
                    print '\r' + '                  ' + '%s%s%s%s%s%s' % (r, old_text, p, char.upper(), r, text[i + 1:]),
                    sys.stdout.flush()
                time.sleep(0.1)

            num += 1


    sys.stdout.write('\x1b]2;Bot Create SSH - @Mr.A_S\x07')
    os.system('clear')
    print '\n\n\n\n\n\n\n\n\n'
    for i in range(random.randrange(1, 2)):
        loading('mohon maaf tunggu sebentar ya...')

    print '\r' + b + ('[' + p + ' ^_< ' + b + ']' + p + '  Thanks For Using My Tools  ' + b + '[' + p + ' ^_< ' + b + ']').center(110)
    time.sleep(1)
    try:
        if open('/sdcard/Android/data/com.termux/.jet', 'r').read() == time.strftime('%d'):
            os.system('clear')
            print p + gagal
            print
            print p + '+' + b + ('=').center(66, '=') + p + '+'
            cl.printf('Mohon Maaf Kamu Hanya Bisa Membuat SSH 2 Kali Dalam 1 Hari')
            cl.printf(' ')
            cl.printf('Jangan Lupa Subscribe, Like & Share Agar Channel ini')
            cl.printf('Semakin Berkembang & Memberikan Tutorial / Tools Terbaru')
            cl.printf(' ')
            cl.printf('https://www.youtube.com/c/MrAS7')
            print p + '+' + b + ('=').center(66, '=') + p + '+'
            try:
                os.remove('/sdcard/Android/data/com.termux/.jet1')
            except:
                pass

        else:
            os.remove('/sdcard/Android/data/com.termux/.jet')
            men = menu()
            getreq()
    except:
        men = main()
        start()

    try:
        if len(open('/sdcard/Android/data/com.termux/.jet1', 'r').read().split(',')) == 3:
            with open('/sdcard/Android/data/com.termux/.jet', 'w') as (Files):
                Files.write(time.strftime('%d'))
            sys.exit()
    except:
        pass
