#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("error")
        return
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("error")
            return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    count = 1
    for attendee in attendees:
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")
        invitation = template.replace("{name}", name)
        invitation = invitation.replace("{event_title}", event_title)
        invitation = invitation.replace("{event_date}", event_date)
        invitation = invitation.replace("{event_location}", event_location)

        filename = f"output_{count}.txt"
        with open(filename, "w") as file:
            file.write(invitation)

        count += 1

