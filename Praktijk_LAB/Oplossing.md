Eerst hebben we de basisconfiguratie opgezet via een statische route. Hierbij verkreeg mijn laptop een IP-adres via DHCP en kon ik een ping uitvoeren naar Google op 8.8.8.8.

![Afbeelding 1](./images/oplossing_basic_lab.png)

Daarna hebben we de standaardroute toegevoegd:

![Afbeelding 2](./images/default_route.png)

Vervolgens hebben we een ping uitgevoerd naar de router in het datacenter:

![Afbeelding 3](./images/ping.png)

Na het toevoegen van de DHCP-helper zijn we een tunnel gaan opzetten:

![Afbeelding 4](./images/dhcp_helper.png)

Ten slotte hebben we de tunnel getest door een ping naar de tunnelbestemming uit te voeren:

![Afbeelding 5](./images/tunnel_setup.png)

Dit was de laatste stap in ons proces, waarbij ik met succes de bestemming van de tunnel kon pingen:

![Afbeelding 6](./images/tracert_tunnel_test.png)
