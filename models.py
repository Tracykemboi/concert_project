from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create a base class for declarative class definitions
Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'

    # Define columns for the bands table
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)

    # Establish a one-to-many relationship with Concert
    concerts = relationship('Concert', back_populates='band')

    def play_in_venue(self, venue, date):
        """
        Create a new concert for this band at the given venue and date.
        
        :param venue: Venue object where the concert will be held
        :param date: Date of the concert (as a string)
        :return: Newly created Concert object
        """
        new_concert = Concert(date=date, band=self, venue=venue)
        session.add(new_concert)
        session.commit()
        return new_concert

    def all_introductions(self):
        """
        Generate introductions for all concerts by this band.
        
        :return: List of introduction strings
        """
        return [concert.introduction() for concert in self.concerts]

    @classmethod
    def most_performances(cls):
        """
        Find the band with the most performances.
        
        :return: Band object with the most concerts
        """
        bands = session.query(cls).all()
        return max(bands, key=lambda band: len(band.concerts))

class Venue(Base):
    __tablename__ = 'venues'

    # Define columns for the venues table
    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)

    # Establish a one-to-many relationship with Concert
    concerts = relationship('Concert', back_populates='venue')

    def concert_on(self, date):
        """
        Find a concert at this venue on the given date.
        
        :param date: Date to search for (as a string)
        :return: Concert object if found, None otherwise
        """
        return session.query(Concert).filter(Concert.venue == self, Concert.date == date).first()

    def most_frequent_band(self):
        """
        Find the band that has performed most often at this venue.
        
        :return: Band object that has performed most often, or None if no concerts
        """
        band_counts = {}
        for concert in self.concerts:
            band_counts[concert.band] = band_counts.get(concert.band, 0) + 1
        return max(band_counts, key=band_counts.get) if band_counts else None

class Concert(Base):
    __tablename__ = 'concerts'

    # Define columns for the concerts table
    id = Column(Integer, primary_key=True)
    date = Column(String)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    # Establish many-to-one relationships with Band and Venue
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def hometown_show(self):
        """
        Check if this concert is in the band's hometown.
        
        :return: True if the concert is in the band's hometown, False otherwise
        """
        return self.band.hometown == self.venue.city

    def introduction(self):
        """
        Generate an introduction for this concert.
        
        :return: String introduction for the band at this concert
        """
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

# Create engine and session
engine = create_engine('sqlite:///concert.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)