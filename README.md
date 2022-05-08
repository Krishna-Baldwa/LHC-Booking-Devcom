# LHC-Booking-Devcom
The url for the admin page is http://127.0.0.1:8000/admin/
Superuser username: Krishna
          password: admin
The url to display the rest-framework page is http://127.0.0.1:8000/halls/
I have used the words unoccupied for hall which is not booked and occupied for the halls which are booked
For getting the data for which all halls are unoccupied run the following commands in the terminal after opening the code in vscode:
python manage.py shell
from Records.models import halls
halls.objects.filter(Occupancy_status="Unoccupied")



