# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def convert_seconds(seconds):
    hours = int(seconds / 3600)
    seconds = seconds - (hours * 3600)
    minutes = int(seconds / 60)
    seconds = seconds - (minutes * 60)
    
    hour_str = ""
    min_str = ""
    sec_str = ""
    
    if hours == 1:
        hour_str = str(hours) + " hour, "
    else:
        hour_str = str(hours) + " hours, "
    
    if minutes == 1:
        min_str = str(minutes) + " minute, "
    else:
        min_str = str(minutes) + " minutes, "
        
    if seconds == 1:
        sec_str = str(seconds) + " second"
    else:
        sec_str = str(seconds) + " seconds"
    
    return hour_str + min_str + sec_str

def download_time(file_size, file_unit, bandwidth, band_unit):
    file_bits = 0
    band_bits = 0
    
    
    if file_unit == "kb":
        file_bits = file_size * 2 ** 10
    elif file_unit == "kB":
        file_bits = file_size * 2 ** 10 * 8
    elif file_unit == "Mb":
        file_bits = file_size * 2 ** 20
    elif file_unit == "MB":
        file_bits = file_size * 2 ** 20 * 8
    elif file_unit == "Gb":
        file_bits = file_size * 2 ** 30
    elif file_unit == "GB":
        file_bits = file_size * 2 ** 30 * 8
    elif file_unit == "Tb":
        file_bits = file_size * 2 ** 40
    elif file_unit == "TB":
        file_bits = file_size * 2 ** 40 * 8
        
    if band_unit == "kb":
        band_bits = bandwidth * 2 ** 10
    elif band_unit == "kB":
        band_bits = bandwidth * 2 ** 10 * 8
    elif band_unit == "Mb":
        band_bits = bandwidth * 2 ** 20
    elif band_unit == "MB":
        band_bits = bandwidth * 2 ** 20 * 8
    elif band_unit == "Gb":
        band_bits = bandwidth * 2 ** 30
    elif band_unit == "GB":
        band_bits = bandwidth * 2 ** 30 * 8
    elif band_unit == "Tb":
        band_bits = bandwidth * 2 ** 40
    elif band_unit == "TB":
        band_bits = bandwidth * 2 ** 40 * 8
        
        # b / (b/s)
        
    seconds = (1.0 * file_bits) / (1.0 * band_bits)
    return convert_seconds(seconds)


print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

