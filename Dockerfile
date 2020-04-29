FROM python
MAINTAINER harshitgarg2006@gmail.com , 7300243823
RUN apt-get update
COPY main.py /rail-reservation/main.py
COPY ticket_booking.py /rail-reservation/ticket_booking.py
COPY checkouts.py /rail-reservation/checkouts.py
CMD python /rail-reservation/main.py
