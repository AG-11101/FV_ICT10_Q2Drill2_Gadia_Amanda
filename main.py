
from pyscript import document

# Members organized by grade level
Grade_7 = [
    "Mister Crabs", "Sponge bob", "Sandy Cheeks",
    "Squidward", "Plankton", "Patrick Star",
    "Ms. Puff", "Gumball"
]

Grade_8 = [
    "Darwin", "Ananais", "Richard", "Penny",
    "Peter Parker", "Gwen Stacy", "Mary Jane",
    "Ben Riley", "Eddie Brock", "Bruce wane"
]

Grade_9 = [
    "Jason Todd", "Dick Grayson"
]

Grade_10 = [
    "Damian Wane", "Freddy", "Vanessa"
]


# Function triggered by the Check button
def check_membership(event=None) -> None:

    # Get the names from the HTML input fields
    first_name = document.getElementById(
        "first_name"
    ).value.strip().title()

    last_name = document.getElementById(
        "last_name"
    ).value.strip().title()

    output = document.getElementById("output1")

    # Make sure both fields are completed
    if not first_name or not last_name:
        output.innerHTML = """
            <div style="color: #9b4050;">
                ✦ ENTRY INCOMPLETE ✦<br>
                Please enter both your first and last name.
            </div>
        """
        return

    # Combine the names
    full_name = f"{first_name} {last_name}"

    # Convert grade lists into sets
    grade_7 = set(Grade_7)
    grade_8 = set(Grade_8)
    grade_9 = set(Grade_9)
    grade_10 = set(Grade_10)

    # Combine all existing members
    master_set = (
        grade_7 | grade_8 | grade_9 | grade_10
    )

    # Check whether the person is already a member
    if full_name in master_set:
        output.innerHTML = f"""
            <div style="color: #667da8;">
                ✦ MEMBER IDENTIFIED ✦<br><br>
                Welcome back, {full_name}!<br>
                Your name is already in the Literature Club registry.
            </div>
        """
    else:
        # Add the new member to the master set
        master_set.add(full_name)

        # Sort names alphabetically for a neat display
        formatted_members_list = "".join(
            f"<li>{name}</li>"
            for name in sorted(master_set)
        )

        total_count = len(master_set)

        # Display the matching cyber-gothic results
        output.innerHTML = f"""
            <div style="
                color: #191c25;
                font-family: 'DM Mono', monospace;
                text-align: center;
            ">
                <div style="
                    font-size: 11px;
                    letter-spacing: 3px;
                    color: #7185ad;
                ">
                    ✦ ENTRY VERIFIED ✦
                </div>

                <h3 style="
                    font-family: 'Playfair Display', serif;
                    font-size: 25px;
                    margin: 12px 0;
                ">
                    Welcome, {full_name}
                </h3>

                <p style="
                    font-size: 11px;
                    line-height: 1.8;
                ">
                    Your name has been added to this session's
                    Literature Club registry.
                </p>

                <hr style="
                    border: 0;
                    border-top: 1px solid #c7cbd8;
                    margin: 18px 0;
                ">

                <strong style="
                    font-size: 12px;
                    letter-spacing: 2px;
                ">
                    TOTAL MEMBERS: {total_count}
                </strong>

                <details style="
                    text-align: left;
                    margin-top: 18px;
                    border: 1px solid #c7cbd8;
                    padding: 12px;
                ">
                    <summary style="
                        cursor: pointer;
                        font-size: 11px;
                        letter-spacing: 2px;
                    ">
                        VIEW MEMBER REGISTRY ✦
                    </summary>

                    <ul style="
                        padding-left: 24px;
                        margin-top: 14px;
                        font-size: 11px;
                        line-height: 2;
                    ">
                        {formatted_members_list}
                    </ul>
                </details>
            </div>
        """
