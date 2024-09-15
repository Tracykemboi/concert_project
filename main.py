from models import Band, Venue, Concert, session

def main():
    try:
        # Create sample data
        print("Creating sample data...")
        band1 = Band(name="The Rockers", hometown="New York")
        band2 = Band(name="Jazz Cats", hometown="New Orleans")

        venue1 = Venue(title="Madison Square Garden", city="New York")
        venue2 = Venue(title="Red Rocks", city="Morrison")

        # Add sample data to the session and commit
        session.add_all([band1, band2, venue1, venue2])
        session.commit()

        # Create some concerts
        print("Creating concerts...")
        band1.play_in_venue(venue1, "2023-09-15")
        band1.play_in_venue(venue2, "2023-10-01")
        band2.play_in_venue(venue1, "2023-09-20")

        # Demonstrate querying relationships
        print("Band1 venues:", [concert.venue.title for concert in band1.concerts])
        print("Venue1 bands:", [concert.band.name for concert in venue1.concerts])

        # Demonstrate concert_on method
        concert = venue1.concert_on("2023-09-15")
        if concert:
            print("Is hometown show?", concert.hometown_show())
            print("Introduction:", concert.introduction())
        else:
            print("No concert found on 2023-09-15")

        # Demonstrate most_performances method
        most_performances = Band.most_performances()
        print("Band with most performances:", most_performances.name if most_performances else "No performances yet")

        # Demonstrate most_frequent_band method
        most_frequent_band = venue1.most_frequent_band()
        print("Most frequent band at venue1:", most_frequent_band.name if most_frequent_band else "No performances yet")

        # Demonstrate all_introductions method
        print("All introductions for band1:")
        for intro in band1.all_introductions():
            print(intro)

    except Exception as e:
        # Handle any exceptions that occur
        print(f"An error occurred: {e}")
    finally:
        # Always close the session to release resources
        session.close()

if __name__ == "__main__":
    main()