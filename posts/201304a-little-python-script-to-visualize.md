<!--
  .. title: Visalizing DSL tones
  .. date: 2012/05/01
  .. slug: 
-->


A little python script to visualize the quality of dsl tones from zyxel routers.
Tested with O² DSL &amp; Comfort (FW  RAS version: V3.40(AOF.5)D0 | 19.03.2009).
Should work for all routers that supports wan adsl linedata {fear|near}.


<a
href="http://1.bp.blogspot.com/-LKk7c6LsBRA/UV4OxEpd7VI/AAAAAAAAD-M/v2nBedVdFA4/s1600/test.png"
style="margin-left: auto; margin-right: auto;"><img border="0" height="301"
src="http://1.bp.blogspot.com/-LKk7c6LsBRA/UV4OxEpd7VI/AAAAAAAAD-M/v2nBedVdFA4/s400/test.png"
width="400"></a>

    :::python
    #!/usr/bin/python

    from pexpect import spawn,EOF
    import sys
    from StringIO import StringIO

    ADDR = "192.168.2.1"
    PASS = "xxxxxxx" #<- here password

    #retrieve values via telnet
    telnet = spawn('telnet %s' % ADDR)

	telnet.expect(': ')
	telnet.sendline('admin')
	telnet.expect(': ')
	telnet.sendline(PASS)

    telnet.expect('ras> ')
	UP = StringIO()
    telnet.logfile_read = UP
    telnet.sendline('wan adsl linedata far')
    telnet.expect('ras> ')

    DOWN = StringIO()
    telnet.logfile_read = DOWN
    telnet.sendline('wan adsl linedata near')
    telnet.expect('ras> ')
    telnet.sendline('exit')
    telnet.expect(EOF)

    UP,DOWN = UP.getvalue(), DOWN.getvalue()

    def parse_data_array(string):
        array = []
        useableChars = '0123456789abcdef'
        for line in string.split("\n"):
           if line.startswith('tone'):
             pos = line.find(':') + 1
             rest = line[pos:]            
             for v in rest:
             if v in useableChars:
                 array.append(int(v, 16))
         return array


    dup = parse_data_array(UP)
    ddown = parse_data_array(DOWN)


    all = sum(dup) + sum(ddown) 
    max = len(ddown)15.0
    print(all/max)

    from matplotlib.pyplot import 

    TONE_WIDTH = 4.3125 #kHz
    x_axis = [i * TONE_WIDTH for i in range(len(dup))]

    pup   = bar(x_axis, dup,   TONE_WIDTH, color = 'r' ,linewidth=0)
    pdown = bar(x_axis, ddown, TONE_WIDTH, color = 'b' ,linewidth=0)

    title('DSL tones')
    yticks(range(0,16))
    ylabel("Bit/chan")
    xlabel("freq [kHz]")
    legend( (pup[0], pdown[0]), ('Up', 'Down'))
    show()
