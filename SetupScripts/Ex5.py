# Ex5
# This file may be added to the --custom argument of mn OR the code copied and pasted to the topology file


def setup_host5(net):
    # Host 5
    h5 = net.get('h5')
    h5.cmd('sudo ifconfig h5-eth0 inet6 add 3000::254/64'.split(' '))
    h5.cmd('sudo route -A inet6 add 2021:0:0::/64 gw 3000::'.split(' '))


def setup_host1(net):
    # Host 1
    h1 = net.get('h1')
    setup_default_host_config(net, 1)
    h1.cmd('sudo ifconfig h1-eth1 up'.split(' '))
    h1.cmd('sudo ifconfig h1-eth1 inet6 add 3000::1/64'.split(' '))


def setup_default_host_config(net, host_number):
    # Host X
    host = net.get('h' + str(host_number))
    host.cmd(('echo 0 > /proc/sys/net/ipv6/conf/h' +
             str(host_number) + '-eth0/accept_ra').split(' '))
    host.cmd(('echo 1 > /proc/sys/net/ipv6/conf/h' +
             str(host_number) + '-eth0/forwarding').split(' '))
    host.cmd(('sudo ifconfig h' + str(host_number) +
             '-eth0 inet6 add 2021::' + str(host_number) + '/128').split(' '))


def setup_all_hosts(self, line):
    net = self.mn
    setup_host5(net)
    setup_host1(net)
    setup_default_host_config(net, 2)
    setup_default_host_config(net, 3)
    setup_default_host_config(net, 4)


CLI.do_chconf = setup_all_hosts
