print_tasks = [
    [64, 93, 35, 38, 97, 16, 79, 36, 81, 28, 58, 77, 31, 11, 51, 73, 86, 32, 48, 47, 61],
    [48, 47, 21, 78, 12, 26, 71, 24, 13],
    [46, 55, 69, 32, 87, 26, 61, 12, 71, 45, 66, 86, 37, 91, 22, 78, 21, 96, 73, 94, 18],
    [16, 79, 81, 28, 77, 31, 73, 61, 94, 21, 37, 18, 39, 45, 66],
    [73, 86, 51, 91, 78, 94, 26, 15, 12, 61, 31, 21, 47, 11, 18, 32, 55, 46, 66],
    [85, 54, 15, 67, 77, 35, 97, 42, 31],
    [91, 24, 64, 93, 65, 16, 79],
    [36, 81, 28, 58, 77, 15, 11, 86, 32, 47, 61, 21, 37, 39, 45, 55, 46],
    [13, 94, 12, 55, 45, 18, 91, 46, 96, 39, 78, 61, 48, 21, 69, 87, 37, 22, 71, 26, 47, 66, 24],
    [85, 77, 35, 28, 42, 13, 15, 58, 97],
    [35, 38, 97, 16, 36, 81, 28, 31, 11, 51, 48, 47, 61, 94, 21],
    [77, 15, 31, 11, 51, 73, 86, 32, 48, 47, 94, 21, 39, 45, 66, 55, 46, 78, 91, 12, 96],
    [28, 51, 66, 79, 58, 45, 77, 15, 48, 21, 36, 39, 61, 32, 86, 16, 73, 94, 37, 31, 18, 11, 81],
    [35, 93, 28, 15, 24, 97, 11, 67, 77, 16, 38, 36, 65, 58, 31, 64, 29, 79, 72],
    [36, 48, 85, 51, 28, 77, 31, 81, 11],
    [94, 81, 31, 48, 18, 51, 28, 36, 37, 86, 58, 11, 45, 61, 47, 39, 77, 85, 15, 21, 16],
    [18, 78, 87, 24, 29],
    [16, 81, 15, 31, 73, 32, 47, 21, 18, 39, 66],
    [97, 64, 67, 15, 72, 36, 77, 31, 22],
    [39, 54, 69, 18, 47, 24, 37, 32, 26, 66, 71, 91, 94, 45, 46],
    [31, 86, 37, 73, 15, 21, 91, 66, 39, 46, 51, 77, 11, 96, 55, 94, 18],
    [91, 96, 71, 42, 64, 93, 35, 85, 16],
    [58, 77, 93, 16, 38, 54, 97, 85, 67, 15, 81, 11, 51],
    [86, 32, 47, 94, 37, 18, 45, 55, 46, 91, 12, 96, 26, 69, 24],
    [93, 24, 36, 67, 97, 28, 77, 79, 13, 81, 71, 64, 69, 38, 29, 22, 42, 54, 58, 85, 35, 16, 65],
    [35, 85, 36, 58, 11, 32, 48, 47, 94],
    [11, 35, 86, 28, 32, 67, 36, 81, 16],
    [81, 58, 15, 73, 94, 21, 37, 66, 55, 46, 78],
    [37, 55, 28, 48, 51, 81, 45, 73, 47, 58, 66, 79, 15, 11, 18, 31, 86, 77, 94],
    [32, 48, 47, 61, 94, 21, 37, 18, 45, 66, 55, 46, 78, 12, 96, 26, 87, 69, 22, 24, 54],
    [48, 47, 94, 21, 37, 18, 39, 45, 66, 55, 46, 78, 91, 12, 96, 26, 87, 71, 69, 22, 24, 54, 13],
    [31, 86, 47, 21, 66, 46, 78, 96, 87],
    [38, 97, 85, 16, 79, 36, 81, 28, 58, 15, 31, 11, 51, 73, 86, 32, 48, 61, 94, 21, 37],
    [39, 66, 55, 46, 78, 91, 26, 87, 71, 69, 22, 24, 54, 13, 29, 67, 42, 72, 64, 93, 35],
    [65, 85, 16, 36, 28, 86, 48, 61, 94, 21, 18],
    [73, 86, 48, 12, 51, 96, 46, 69, 32, 91, 66],
    [58, 77, 15, 31, 11, 73, 86, 32, 48, 47, 61, 21, 39, 45, 55, 46, 12],
    [48, 39, 15, 28, 85],
    [22, 54, 67, 38, 16, 28, 58],
    [78, 12, 87, 42, 72, 38, 16],
    [69, 64, 71, 67, 29, 87, 55, 35, 24, 91, 65, 42, 97, 46, 93, 72, 26],
    [32, 48, 47, 61, 21, 18, 39, 45, 66, 55, 46, 78, 91, 12, 96, 87, 71, 69, 22, 24, 54],
    [11, 73, 32, 47, 18, 39, 66, 55, 46, 78, 12, 96, 26, 87, 71],
    [12, 55, 73, 32, 48, 87, 39, 21, 94, 18, 61, 91, 45, 37, 46, 69, 26, 86, 96],
    [71, 69, 24, 54, 13, 67, 42, 64, 35, 65, 97, 85, 16, 79, 36, 81, 28, 58, 77],
    [67, 72, 64, 35, 97, 85, 16, 81, 28, 15, 11, 73, 32],
    [86, 97, 48, 51, 32, 58, 65, 36, 73, 93, 28, 11, 38, 61, 64, 31, 47, 81, 77, 35, 15, 79, 16],
    [94, 21, 37, 18, 39, 45, 46, 78, 96, 69, 22, 24, 29, 67, 42],
    [71, 69, 22, 54, 13, 29, 67, 42, 72, 64, 93, 35, 85, 16, 79, 36, 28, 58, 77],
    [45, 66, 46, 78, 26, 87, 71, 69, 22, 13, 29, 67, 42, 72, 93, 35, 38],
    [21, 18, 39, 45, 55, 91, 12, 26, 87, 71, 24, 13, 42],
    [26, 46, 94, 69, 66, 47, 91, 96, 24, 37, 22, 13, 61, 29, 87],
    [47, 72, 93, 81, 51, 11, 38, 48, 64, 32, 77, 35, 65],
    [37, 18, 39, 55, 46, 12, 96, 87, 22, 24, 54, 13, 72],
    [12, 46, 35, 64, 85, 71, 26],
    [28, 58, 77, 31, 51, 73, 86, 32, 48, 47, 61, 37, 18, 39, 45, 66, 55, 46, 91],
    [86, 32, 48, 47, 61, 94, 21, 37, 18, 45, 66, 55, 46, 78, 91, 12, 96, 26, 87, 71, 69, 22, 24],
    [78, 12, 96, 13, 67, 72, 64, 93, 85],
    [78, 91, 12, 96, 26, 87, 71, 22, 24, 54, 13, 29, 42, 72, 64, 93, 35, 38, 65, 85, 16],
    [38, 71, 42, 29, 97, 87, 12, 78, 16],
    [96, 87, 22, 24, 54, 67, 72, 93, 85, 36, 81],
    [86, 61, 94, 39, 45, 66, 55, 46, 78, 71, 69],
    [94, 96, 46, 86, 31, 91, 26, 61, 11, 48, 47, 18, 32, 66, 51, 37, 15],
    [48, 47, 61, 94, 21, 18, 39, 45, 55, 46, 78, 91, 12, 26, 87, 71, 69, 22, 24, 54, 13],
    [67, 81, 58, 77, 31],
    [12, 71, 54, 37, 39, 29, 91, 96, 64, 69, 87, 78, 46, 13, 26, 22, 24],
    [54, 72, 38, 16, 81, 15, 51],
    [21, 47, 81, 31, 39, 51, 77, 11, 32, 73, 36, 15, 16, 28, 85, 37, 97, 86, 48],
    [78, 96, 69, 91, 55, 66, 12, 13, 54, 47, 46, 45, 21, 26, 18],
    [96, 69, 54, 72, 64, 79, 81],
    [65, 36, 15, 11, 51, 21, 18],
    [94, 21, 37, 18, 39, 45, 66, 55, 78, 91, 12, 96, 26, 87, 71, 69, 22, 24, 54, 13, 29, 67, 42],
    [38, 65, 97, 85, 16, 79, 36, 81, 28, 58, 77, 15, 31, 11, 51, 73, 32, 48, 47, 61, 94, 21, 37],
    [22, 67, 85, 24, 93, 77, 72, 35, 69, 16, 15, 64, 97, 28, 81, 42, 38],
    [39, 61, 66, 51, 36, 46, 18],
    [94, 73, 39, 51, 45, 55, 78, 66, 46, 15, 48, 47, 12, 32, 37, 26, 18, 31, 86],
    [13, 16, 22, 69, 78, 65, 12, 26, 87, 38, 85, 96, 71],
    [39, 28, 15, 79, 21, 47, 73, 36, 37, 48, 11, 58, 77, 81, 45, 61, 31],
    [72, 37, 91, 12, 26, 18, 78, 66, 42, 64, 87, 46, 55, 45, 96, 24, 29],
    [65, 79, 93, 69, 36, 38, 72, 58, 71, 29, 85, 42, 67, 54, 24, 35, 13, 64, 87, 97, 28, 16, 81],
    [12, 96, 29, 67, 72, 38, 65, 85, 36],
    [29, 54, 12, 69, 13, 91, 78, 64, 67, 35, 26, 93, 24, 46, 96],
    [13, 35, 65, 85, 16, 79, 81, 58, 77, 51, 73],
    [66, 46, 12, 55, 69, 61, 39, 71, 67, 37, 18, 45, 94, 21, 13, 26, 96],
    [16, 11, 29, 77, 15, 72, 36, 51, 67, 58, 64, 93, 79, 73, 97, 38, 86, 65, 42, 85, 31, 35, 28],
    [51, 73, 32, 47, 61, 94, 37, 18, 39, 45, 66, 55, 78, 91, 26],
    [85, 51, 73, 79, 94, 86, 61, 16, 47, 65, 37, 97, 18, 32, 28, 21, 15, 48, 11, 31, 77, 36, 58],
    [45, 66, 55, 46, 26, 71, 22, 54, 13, 67, 42, 35, 38],
    [81, 28, 58, 77, 15, 31, 11, 51, 73, 86, 32, 48, 47, 61, 94, 37, 18, 39, 45, 66, 55, 46, 78],
    [36, 28, 15, 31, 73, 86, 32, 48, 47, 61, 94, 21, 37, 18, 45],
    [61, 94, 21, 37, 18, 39, 45, 66, 55, 46, 78, 12, 96, 26, 87, 71, 69, 22, 24, 54, 13, 29, 67],
    [87, 91, 55, 66, 54, 46, 71, 24, 22, 42, 29, 69, 12, 93, 35, 39, 26, 72, 13],
    [29, 67, 42, 72, 64, 93, 35, 38, 97, 85, 16, 79, 36, 81, 58, 77, 15, 11, 51, 73, 86],
    [47, 61, 37, 18, 39, 45, 66, 91, 12, 96, 26, 87, 69, 24, 54, 13, 29],
    [15, 11, 51, 86, 32, 48, 47, 94, 37, 39, 45, 66, 55, 78, 12, 96, 26],
    [71, 61, 78, 48, 26, 18, 55, 45, 96, 54, 94, 39, 66, 24, 32, 21, 91],
    [28, 66, 55, 94, 77],
    [97, 67, 24, 16, 64, 69, 26, 93, 78, 13, 72],
    [79, 36, 81, 28, 58, 77, 15, 31, 11, 51, 73, 86, 32, 48, 47, 61, 21, 37, 18, 39, 45, 66, 55],
    [22, 54, 29, 67, 42, 72, 64, 93, 38, 16, 79, 36, 81, 28, 58, 15, 31],
    [11, 86, 51, 48, 15, 55, 47, 18, 96, 32, 91],
    [38, 26, 54, 42, 35, 69, 96, 45, 78, 22, 29, 46, 91, 72, 64, 24, 71, 12, 66],
    [58, 77, 15, 11, 73, 86, 32, 48, 47, 21, 37, 66, 46, 78, 12],
    [54, 29, 42, 72, 64, 35, 38, 16, 79, 36, 58, 11, 51],
    [11, 55, 66, 87, 94, 61, 47, 86, 71, 91, 39, 96, 21, 73, 48, 51, 45],
    [86, 61, 96, 73, 66, 77, 21, 47, 48, 18, 11, 78, 45, 46, 94, 12, 51, 31, 32, 15, 37],
    [29, 67, 42, 64, 93, 35, 38, 65, 97, 85, 16, 79, 36, 81, 28, 77, 15, 11, 51, 73, 86],
    [93, 38, 65, 81, 28, 58, 15],
    [31, 81, 24, 36, 38, 93, 97, 64, 11, 28, 77, 35, 42, 54, 79, 67, 72, 13, 16, 29, 58],
    [65, 97, 79, 36, 81, 77, 51, 73, 21, 37, 18],
    [28, 86, 47, 18, 39, 45, 55],
    [18, 48, 69, 26, 91, 32, 39, 94, 86, 37, 21, 47, 96, 78, 45, 55, 87, 66, 24, 61, 46],
    [15, 51, 73, 86, 32, 47, 94, 21, 37, 45, 55, 91, 26],
    [24, 46, 67, 72, 91, 69, 64, 22, 26, 29, 93, 71, 13, 54, 96, 78, 12, 38, 87, 97, 65],
    [67, 93, 38, 85, 36, 28, 58],
    [85, 72, 29, 35, 67, 22, 31],
    [81, 28, 15, 31, 11, 86, 48, 47, 61, 94, 21, 37, 18, 39, 45, 66, 55, 46, 78],
    [35, 16, 64, 77, 81, 15, 36, 93, 86, 85, 38, 11, 51, 72, 47, 79, 97],
    [45, 66, 46, 61, 15, 86, 78, 39, 94, 18, 51, 48, 77, 73, 31, 37, 32, 21, 47, 58, 81],
    [71, 24, 67, 42, 65, 79, 36, 81, 28, 58, 77],
    [61, 86, 11, 18, 36, 39, 48, 94, 15, 77, 28, 47, 55, 37, 58, 21, 45, 51, 73],
    [13, 29, 72, 64, 93, 38, 65, 97, 85, 16, 79, 36, 81, 28, 58, 77, 15, 31, 11, 51, 73],
    [15, 97, 16, 54, 85, 42, 31, 28, 22, 93, 81],
    [71, 67, 26, 66, 18, 45, 78, 12, 61],
    [38, 54, 85, 67, 36, 29, 24, 65, 64, 96, 71, 12, 26, 97, 16, 93, 79, 72, 35, 42, 22],
    [12, 86, 45, 31, 47, 51, 94, 37, 96, 21, 18],
    [96, 72, 13, 21, 69, 71, 78],
    [86, 48, 37, 55, 46, 91, 71, 69, 22],
    [26, 55, 66, 48, 94, 71, 45, 12, 32, 11, 96, 86, 61],
    [15, 97, 29, 31, 28, 64, 38, 35, 93, 51, 85, 65, 73, 36, 77, 16, 67, 11, 42],
    [21, 37, 18, 39, 45, 66, 55, 46, 78, 91, 12, 96, 26, 87, 71, 69, 22, 54, 13, 29, 67, 42, 72],
    [45, 51, 36, 73, 31, 48, 94, 32, 58, 21, 66, 28, 81, 15, 61, 79, 11, 77, 55],
    [36, 79, 28, 47, 48, 58, 38, 85, 73, 93, 61, 86, 97, 51, 31, 65, 32, 15, 11, 94, 35, 16, 77],
    [91, 12, 22, 29, 64, 65, 79],
    [47, 61, 94, 21, 37, 45, 91, 96, 87, 69, 22, 24, 29],
    [42, 64, 93, 35, 65, 16, 79, 81, 58, 31, 11, 51, 73, 86, 32],
    [37, 13, 71, 21, 39, 69, 66, 46, 96, 12, 24],
    [79, 15, 47, 45, 21, 77, 51, 16, 85],
    [77, 94, 32, 73, 61, 18, 55],
    [66, 55, 46, 78, 91, 12, 96, 26, 71, 69, 22, 24, 54, 13, 29, 67, 42, 72, 64, 93, 35, 38, 65],
    [79, 36, 28, 58, 77, 15, 31, 11, 73, 86, 32, 48, 47, 61, 94, 21, 37, 18, 39, 66, 55],
    [65, 72, 87, 69, 54, 24, 35, 66, 71],
    [26, 24, 13, 29, 42, 72, 64, 93, 65, 85, 16, 79, 28],
    [11, 73, 32, 61, 37, 18, 39, 66, 55, 12, 71],
    [73, 48, 61, 94, 21, 37, 18, 39, 55, 46, 78, 12, 96, 26, 87, 69, 22],
    [93, 48, 35, 97, 47, 85, 81, 77, 61, 28, 31, 94, 15, 65, 51, 58, 86, 73, 11],
    [26, 38, 72, 46, 12, 97, 71, 93, 64, 24, 55, 67, 35],
    [16, 65, 97, 31, 36, 15, 51, 58, 11, 73, 32, 42, 67, 93, 77, 28, 86, 72, 38],
    [32, 31, 87, 51, 91, 47, 21, 11, 37, 73, 46],
    [71, 24, 54, 13, 29, 67, 42, 72, 64, 93, 35, 38, 97, 85, 16, 79, 36, 81, 28, 58, 77],
    [78, 26, 29, 35, 46, 69, 54, 45, 87, 13, 96, 42, 67, 93, 71, 12, 39, 64, 91],
    [37, 79, 94, 28, 31, 36, 77, 61, 97, 86, 51, 11, 16, 48, 18, 85, 65, 47, 58, 81, 32, 73, 21],
    [69, 24, 13, 29, 93, 35, 38, 65, 97],
    [69, 29, 42, 72, 38, 85, 16, 28, 15],
    [42, 72, 64, 38, 65, 97, 16, 79, 36, 81, 28, 58, 15, 51, 73, 86, 48],
    [86, 61, 94, 21, 18, 39, 66, 91, 12, 96, 71, 69, 24],
    [37, 39, 45, 66, 55, 78, 91, 96, 26, 87, 71, 69, 24, 13, 29],
    [85, 79, 81, 28, 15, 31, 11, 51, 86, 32, 47, 94, 21, 37, 18, 39, 45],
    [64, 54, 65, 85, 38, 69, 16, 67, 26, 42, 13, 97, 29, 79, 36, 12, 87, 35, 96],
    [78, 24, 71, 97, 55, 96, 29],
    [45, 66, 55, 46, 78, 91, 12, 96, 26, 87, 69, 24, 29, 42, 64, 35, 38],
    [31, 51, 73, 86, 32, 94, 21, 18, 45, 66, 87],
    [54, 13, 67, 64, 93, 35, 38, 65, 97, 79, 36, 28, 58, 77, 31, 11, 51],
    [61, 21, 37, 45, 66, 78, 12, 96, 69, 22, 24, 54, 13, 29, 67],
    [12, 39, 31, 55, 37, 78, 58],
    [26, 61, 18, 22, 45, 67, 46, 37, 69, 94, 12],
    [86, 32, 48, 47, 61, 94, 21, 37, 18, 39, 45, 66, 55, 46, 78, 91, 12, 26, 87, 71, 69, 22, 24],
    [77, 31, 51, 48, 94, 21, 37, 18, 66, 55, 78, 91, 12],
    [67, 94, 96, 12, 29, 18, 39, 13, 26, 71, 78, 46, 45, 21, 69, 55, 66],
    [48, 94, 21, 37, 39, 45, 66, 55, 46, 78, 71, 69, 22, 24, 13],
    [69, 46, 32, 47, 55, 48, 45, 94, 21, 87, 78, 61, 39, 12, 73, 18, 86, 51, 26, 37, 66],
    [37, 39, 45, 66, 55, 78, 91, 12, 87, 71, 69, 22, 24, 54, 72],
    [78, 91, 12, 96, 26, 71, 69, 22, 24, 54, 13, 67, 42, 72, 64, 35, 65, 85, 16],
    [21, 37, 18, 39, 45, 55, 46, 78, 91, 12, 96, 26, 87, 71, 69, 22, 24, 54, 13, 29, 67, 42, 72],
    [37, 58, 21, 94, 55, 39, 86, 45, 18, 11, 46, 31, 66, 36, 15],
    [37, 18, 39, 48, 46, 47, 81, 15, 61, 11, 58, 77, 66, 51, 21, 94, 55, 36, 31],
    [61, 94, 45, 47, 78, 46, 13, 26, 39, 54, 22, 69, 48, 18, 37],
    [73, 77, 47, 58, 61, 12, 91, 11, 18, 31, 45, 86, 32, 21, 55],
    [15, 45, 31, 32, 86, 16, 61, 48, 85, 28, 11, 37, 21, 73, 58, 18, 47],
    [65, 97, 85, 16, 79, 36, 81, 58, 77, 15, 31, 11, 51, 73, 86, 32, 48, 47, 61, 94, 21, 37, 18],
    [46, 91, 12, 96, 71, 22, 13, 29, 65, 97, 85],
    [54, 29, 64, 93, 65, 85, 16, 31, 51],
    [87, 22, 24, 54, 13, 29, 67, 42, 72, 64, 93, 35, 38, 65, 97, 16, 79, 36, 81, 28, 58],
    [64, 22, 91, 87, 38, 26, 42, 72, 13, 67, 65, 55, 69, 29, 93, 71, 78, 35, 24, 96, 46],
    [64, 24, 13, 26, 72, 39, 55],
    [85, 11, 36, 86, 35, 42, 16, 64, 51, 72, 38, 93, 79, 81, 48, 31, 58],
    [38, 32, 58, 64, 97, 81, 16, 73, 31, 85, 51, 42, 93, 35, 11, 86, 65, 72, 36, 79, 28, 67, 77],
    [66, 55, 46, 78, 12, 96, 26, 87, 71, 69, 22, 24, 54, 13, 29, 67, 42, 64, 93, 35, 38],
    [18, 66, 78, 22, 67],
    [37, 66, 46, 91, 96, 87, 71, 69, 24, 13, 29, 72, 64],
    [37, 39, 45, 66, 55, 46, 78, 12, 96, 71, 69, 22, 54, 29, 42, 72, 64],
    [96, 91, 66, 77, 48, 73, 55, 51, 32, 86, 61, 47, 18, 94, 15],
    [32, 48, 47, 61, 37, 18, 39, 45, 66, 55, 46, 78, 91, 12, 96, 87, 71, 69, 22, 24, 54],
    [72, 93, 38, 16, 79, 28, 15, 11, 51, 86, 32, 48, 47],
    [15, 31, 51, 73, 86, 32, 47, 61, 94, 37, 18, 45, 91, 96, 26],
    [69, 24, 29, 67, 93, 38, 65, 28, 15]
]