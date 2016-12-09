import random

colors = [['#B20008', '#FF2B34'],
          ['#FF2B34', '#B20008'],
          ['#E6000A', '#FF2B34'],
          ['#FF2B34', '#E6000A'],
          ['#FFADCE', '#FF2B34'],
          ['#9A5200', '#FF2B34'],
          ['#FF2B34', '#9A5200'],
          ['#FF8F00', '#FF2B34'],
          ['#FF2B34', '#FF8F00'],
          ['#FFC169', '#FF2B34'],
          ['#807500', '#FF2B34'],
          ['#FF2B34', '#807500'],
          ['#BE9E00', '#FF2B34'],
          ['#FF2B34', '#BE9E00'],
          ['#F8E800', '#FF2B34'],
          ['#008009', '#FF2B34'],
          ['#FF2B34', '#008009'],
          ['#00B20D', '#FF2B34'],
          ['#FF2B34', '#00B20D'],
          ['#8BFF7A', '#FF2B34'],
          ['#00588C', '#FF2B34'],
          ['#FF2B34', '#00588C'],
          ['#005FE4', '#FF2B34'],
          ['#FF2B34', '#005FE4'],
          ['#BCCDFF', '#FF2B34'],
          ['#5E008C', '#FF2B34'],
          ['#FF2B34', '#5E008C'],
          ['#7F00BF', '#FF2B34'],
          ['#FF2B34', '#7F00BF'],
          ['#D1A3FF', '#FF2B34'],
          ['#9A5200', '#FF8F00'],
          ['#FF8F00', '#9A5200'],
          ['#C97E00', '#FF8F00'],
          ['#FF8F00', '#C97E00'],
          ['#FFC169', '#FF8F00'],
          ['#807500', '#FF8F00'],
          ['#FF8F00', '#807500'],
          ['#BE9E00', '#FF8F00'],
          ['#FF8F00', '#BE9E00'],
          ['#F8E800', '#FF8F00'],
          ['#008009', '#FF8F00'],
          ['#FF8F00', '#008009'],
          ['#00B20D', '#FF8F00'],
          ['#FF8F00', '#00B20D'],
          ['#8BFF7A', '#FF8F00'],
          ['#00588C', '#FF8F00'],
          ['#FF8F00', '#00588C'],
          ['#005FE4', '#FF8F00'],
          ['#FF8F00', '#005FE4'],
          ['#BCCDFF', '#FF8F00'],
          ['#5E008C', '#FF8F00'],
          ['#FF8F00', '#5E008C'],
          ['#A700FF', '#FF8F00'],
          ['#FF8F00', '#A700FF'],
          ['#D1A3FF', '#FF8F00'],
          ['#B20008', '#FF8F00'],
          ['#FF8F00', '#B20008'],
          ['#FF2B34', '#FF8F00'],
          ['#FF8F00', '#FF2B34'],
          ['#FFADCE', '#FF8F00'],
          ['#807500', '#F8E800'],
          ['#F8E800', '#807500'],
          ['#BE9E00', '#F8E800'],
          ['#F8E800', '#BE9E00'],
          ['#FFFA00', '#EDDE00'],
          ['#008009', '#F8E800'],
          ['#F8E800', '#008009'],
          ['#00EA11', '#F8E800'],
          ['#F8E800', '#00EA11'],
          ['#8BFF7A', '#F8E800'],
          ['#00588C', '#F8E800'],
          ['#F8E800', '#00588C'],
          ['#00A0FF', '#F8E800'],
          ['#F8E800', '#00A0FF'],
          ['#BCCEFF', '#F8E800'],
          ['#5E008C', '#F8E800'],
          ['#F8E800', '#5E008C'],
          ['#AC32FF', '#F8E800'],
          ['#F8E800', '#AC32FF'],
          ['#D1A3FF', '#F8E800'],
          ['#B20008', '#F8E800'],
          ['#F8E800', '#B20008'],
          ['#FF2B34', '#F8E800'],
          ['#F8E800', '#FF2B34'],
          ['#FFADCE', '#F8E800'],
          ['#9A5200', '#F8E800'],
          ['#F8E800', '#9A5200'],
          ['#FF8F00', '#F8E800'],
          ['#F8E800', '#FF8F00'],
          ['#FFC169', '#F8E800'],
          ['#008009', '#00EA11'],
          ['#00EA11', '#008009'],
          ['#00B20D', '#00EA11'],
          ['#00EA11', '#00B20D'],
          ['#8BFF7A', '#00EA11'],
          ['#00588C', '#00EA11'],
          ['#00EA11', '#00588C'],
          ['#005FE4', '#00EA11'],
          ['#00EA11', '#005FE4'],
          ['#BCCDFF', '#00EA11'],
          ['#5E008C', '#00EA11'],
          ['#00EA11', '#5E008C'],
          ['#7F00BF', '#00EA11'],
          ['#00EA11', '#7F00BF'],
          ['#D1A3FF', '#00EA11'],
          ['#B20008', '#00EA11'],
          ['#00EA11', '#B20008'],
          ['#FF2B34', '#00EA11'],
          ['#00EA11', '#FF2B34'],
          ['#FFADCE', '#00EA11'],
          ['#9A5200', '#00EA11'],
          ['#00EA11', '#9A5200'],
          ['#FF8F00', '#00EA11'],
          ['#00EA11', '#FF8F00'],
          ['#FFC169', '#00EA11'],
          ['#807500', '#00EA11'],
          ['#00EA11', '#807500'],
          ['#BE9E00', '#00EA11'],
          ['#00EA11', '#BE9E00'],
          ['#F8E800', '#00EA11'],
          ['#00588C', '#00A0FF'],
          ['#00A0FF', '#00588C'],
          ['#005FE4', '#00A0FF'],
          ['#00A0FF', '#005FE4'],
          ['#BCCDFF', '#00A0FF'],
          ['#5E008C', '#00A0FF'],
          ['#00A0FF', '#5E008C'],
          ['#9900E6', '#00A0FF'],
          ['#00A0FF', '#9900E6'],
          ['#D1A3FF', '#00A0FF'],
          ['#B20008', '#00A0FF'],
          ['#00A0FF', '#B20008'],
          ['#FF2B34', '#00A0FF'],
          ['#00A0FF', '#FF2B34'],
          ['#FFADCE', '#00A0FF'],
          ['#9A5200', '#00A0FF'],
          ['#00A0FF', '#9A5200'],
          ['#FF8F00', '#00A0FF'],
          ['#00A0FF', '#FF8F00'],
          ['#FFC169', '#00A0FF'],
          ['#807500', '#00A0FF'],
          ['#00A0FF', '#807500'],
          ['#BE9E00', '#00A0FF'],
          ['#00A0FF', '#BE9E00'],
          ['#F8E800', '#00A0FF'],
          ['#008009', '#00A0FF'],
          ['#00A0FF', '#008009'],
          ['#00B20D', '#00A0FF'],
          ['#00A0FF', '#00B20D'],
          ['#8BFF7A', '#00A0FF'],
          ['#5E008C', '#AC32FF'],
          ['#AC32FF', '#5E008C'],
          ['#7F00BF', '#AC32FF'],
          ['#AC32FF', '#7F00BF'],
          ['#D1A3FF', '#AC32FF'],
          ['#B20008', '#AC32FF'],
          ['#AC32FF', '#B20008'],
          ['#FF2B34', '#AC32FF'],
          ['#AC32FF', '#FF2B34'],
          ['#FFADCE', '#AC32FF'],
          ['#9A5200', '#AC32FF'],
          ['#AC32FF', '#9A5200'],
          ['#FF8F00', '#AC32FF'],
          ['#AC32FF', '#FF8F00'],
          ['#FFC169', '#AC32FF'],
          ['#807500', '#AC32FF'],
          ['#AC32FF', '#807500'],
          ['#BE9E00', '#AC32FF'],
          ['#AC32FF', '#BE9E00'],
          ['#F8E800', '#AC32FF'],
          ['#008009', '#AC32FF'],
          ['#AC32FF', '#008009'],
          ['#00B20D', '#AC32FF'],
          ['#AC32FF', '#00B20D'],
          ['#8BFF7A', '#AC32FF'],
          ['#00588C', '#AC32FF'],
          ['#AC32FF', '#00588C'],
          ['#005FE4', '#AC32FF'],
          ['#AC32FF', '#005FE4'],
          ['#BCCDFF', '#AC32FF']]


def random_color():
    return random.choice(colors)