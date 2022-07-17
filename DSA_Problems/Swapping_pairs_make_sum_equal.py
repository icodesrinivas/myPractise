

def findSwapValues(a, n, b, m):

    sum_a = sum(a)
    sum_b = sum(b)

    a.sort()
    b.sort()

    target = (sum_a - sum_b) / 2
    if target.is_integer():
        target = (sum_a - sum_b) // 2

    i = 0
    j = 0
    while i < n and j < m:
        diff = a[i] - b[j]
        if diff == target:
            return 1

        if diff < target:
            i += 1
        else:
            j += 1

    return -1

# print(findSwapValues([10,10,10,10], 4, [5,5,5,5], 4))


lis1 = '134 263 800 312 146 553 560 104 795 765 96 415 260 28 6 210 915 547 35 9 353 189 646 231 514 356 312 84 289 365 908 206 500 268 168 624 934 348 463 37 205 296 224 861 568 457 271 945 459 354 905 408 444 138 93 530 486 513 294 276 899 171 454 556 150 743 511 24 689 814 282 842 350 591 975 549 445 426 684 897 584 468 128 279 421 416 592 160 977 503 493 747 935 546 248 985 304 153 145 838 168 950 748 759 793 998 944 170 237 391 123 755 752 427 145 403 684 604 676 632 284 153 205 452 817 777 545 679 655 738 911 870 537 491 728 212 68 587 163 898 578 681 20 726 907 83 5 954 318 439 608 701 715 826 768 529 566 728 280 175 455 144 406 792 986 309 480 484 828 340 387 357 73 468 676 769 694 344 720 13 836 346 771 157 870 733 988 382 603 935 515 725 855 296 456 787 601 74 166 637 250 591 634 814 227 989 838 81 915 181 864 338 175 217 295 878 161 499 796 8 811 951 136 903 489 523 846 441 478 161 608 686 676 710 980 638 627 14 514 830 244 878 427 378 936 448 945 124 589 977 169 576 837 942 794 470 309 937 297 882 97 807 297 23 520 46 591 7 368 562 52 145 188 532 918 540 877 219 254 85 767 308 290 258 649 528 109 481 679 58 695 177 932 518 653 88 415 113 23 856 741 879 454 347 298 804 717 707 660 26 907 682 196 239 967 305 339 881 111 644 705 689 563 965 328 725 534 293 609 29 751 85 157 651 951 437 633 920 677 2 839 463 373 612 786 682 294 378 185 70 938 935 825 43 799 358 613 695 992 195 620 205 967 12 334 476 825 828 469 922 978 808 108 257 790 647 636 530 570 129 950 651 782 455 645 117 641 77 467 683 286 918 131 283 620 77 720 583 477 336 265 172 229 32 790 546 101 182 52 721 463 26 440 519 86 540 27 321 904 844 543 343 135 826 141 324 700 798 180 803 753 410 870 96 819 622 584 413 432 30 826 549 424 434 312 997 988 124 426 351 454 24 333 385 235 447 367 247 782 970 926 788 509 619 988 192 522 334 555 670 734 476 760 231 350 945 125 183 20 347 473 318 936 519 286 481 9 644 889 518 820 126 694 481 438 390 892 277 348 751 379 889 658 569 437 717 507 958 650 544 54 416 820 123 750 907 179 420 621 39 50 88 177 236 176 835 140 989 379 991 645 543 834 682 695 672 250 755 683 502 424 761 497 717 216 79 281 834 729 523 236 686 609 581 924 662 705 783 441 759 989 543 454 992 548 236 558 260 672 204 615 324 555 825 736 171 855 794 375 655 468 290 523 994 138 733 377 365 180 458 965 605 465 717 108 751 985 96 816 968 786 600 645 212 778 379 839 850 956 291 68 329 858 314 420 899 670 81 887 355 247 664 958 729 460 121 89 867 695 193 775 889 52 966 642 575 762 315 498 834 601 387 560 555 658 439 137 286 601 900 878 398 736 591 355 616 507 689 125 42 803 131 617 121 339 876 160 273 662 619 222 320 823 319 448 168 545 161 422 664 840 392 141 969 333 793 106 268 225 429 549 154 753 716 779 564 193 770 860 698 932 462 792 987 942 618 199 780 979 291 61 89 204 127 371 456 517 398 744 691 782 426 894 22 304 740 590 971 366 518 171 97 371 551 949 603 155 238 880 671 326 860 645 335 72 727 958 615 738 587 206 629 610 96 754 420 767 12 153 242 589 230 203 159 436 717 345 883 367 928 132 928 219 276 574 317 282 807 29 271 849 305 906 550 362 680 879 349 506 641 479 977 594 324 919 839 796 764 738 607 284 861 404 842 184 732 317 764 281 165 733 279 784 237 57 882 128 1 532 549 672 569 872 267 394 836 544 438 135 564 436 972 744 511 425 546 502 862 919 145 525 217 787 720 492 28 239 497 895 464 90 267 207 349 561 748 800 985 231 932 210 398 998 208 312 775 933 905 331 651 764 837 128 688 262 360 115 746 225 446 260 303 897 276 76 184 584 896 202 986 980 553 156 554 176 436 107 351 653 664 70 588 581 550 760 549 623 352 422 609 46 946 390 87 366 136 770 204 926 573 591 114 796 616 45 173 114 779 897 366 524 831 985 77 702 1 800 207 23 192 484 952 320 617 237 468 332 717 41 1 894 831 830 17 112 597 684 338 793 720 431 247 178 327 66 93 572 834 731 941 839 923 612 445 815 961 995 184 655 962 902 408 762 952 186 279 447 467 678 424 727 718 30 854'.split(' ')
lis2 = '397 1112 699 664 1560 511 288 216 1462 44 542 877 870 396 654 1114 768 792 1282 500 501 1085 1025 1216 813 1313 582 623 999 570 1070 1010 893 535 1503 1124 941 1524 871 1581 1052 407 837 752 1480 1240 1481 1233 457 983 1118 1507 1791 1114 628 878 1179 548 1288 1308 437 657 1594 1224 1393 1781 1028 940 655 1061 1259 746 990 959 757 1309 1541 1297 1294 455 599 1198 1295 964 1168 744 541 1445 1038 733 1182 928 1603 1370 1538 1240 1151 1243 675 803 841 1448 1216 919 1096 1202 392 1173 660 804 1762 1039 1012 1287 639 1294 1386 1618 641 1344 1122 805 1384 1069 1566 745 1779 1264 1246 1179 904 320 566 598 930 197 720 1458 1096 339 1075 548 1177 590 737 872 1450 741 528 879 1620 801 1102 1424 686 1589 435 1272 1220 755 1394 1528 1053 827 638 836 808 1388 1553 679 1302 985 1468 672 255 1873 868 1157 1308 1187 825 979 810 1653 1391 1786 365 1437 1166 699 1601 1237 762 718 1150 1204 414 697 1303 813 437 261 1336 283 773 489 959 626 348 1748 886 961 465 1498 983 1163 966 1441 997 462 1375 858 1309 1112 777 478 718 682 614 1752 1714 1128 1180 856 1225 1210 991 1295 308 367 791 1455 767 653 1407 946 1175 828 1169 1099 1268 1227 1154 1465 1194 470 943 1657 599 660 138 413 1011 1129 1370 1188 1516 1367 1005 1185 1185 1214 295 1115 1252 922 1190 1586 1488 1200 1532 1446 784 818 876 939 1380 907 1649 1030 758 1517 871 742 638 1570 1182 859 1081 1784 1386 857 1157 1689 1247 397 1172 1319 751 1242 911 1687 581 956 888 1664 1018 1217 1077 1332 988 1115 1097 423 1501 1276 1327 971 1196 167 934 738 1215 433 1281 542 1142 616 706 1086 1232 1110 1126 374 654 703 1469 1343 963 1558 1394 1779 1560 979 1270 150 331 827 915 1435 1208 916 1044 1561 884 268 922 1552 393 1551 1186 980 799 1573 1325 835 706 1174 779 395 819 362 1153 1228 1295 1060 495 891 1089 300 1154 1456 1042 1228 1147 1456 918 1758 1560 1345 1145 1246 916 1081 446 1012 1021 939 129 1081 1241 1139 1230 982 699 1408 1255 971 1364 1064 742 1507 520 736 1359 357 556 1309 1785 1163 608 1206 1087 1838 982 1601 816 622 861 671 563 1173 260 1480 1188 1533 710 612 458 1317 658 1131 1309 975 1031 992 477 502 974 1499 705 1412 218 893 1263 1355 1062 703 1007 215 1436 937 705 1049 42 1725 847 709 1022 1513 678 505 159 1406 1672 1762 1057 1776 1179 1617 1310 1714 465 914 1102 1445 884'.split(' ')
print('len(lis1)',len(lis1))
print('len(lis2)',len(lis2))
lis1 = list(map(int, lis1))
lis2 = list(map(int, lis2))
#
print(findSwapValues(lis1, len(lis1), lis2, len(lis2)))
#
#
# mis1 = '10 570 652 327 862 177 636 293 914 864 317 561 977 526 572 512 299 180 51 171 782 284 792 475 680 504 968 942 930 583 253 562 925 744 825 708 968 254 565 874 97 663 556 653 807 593 652 761 541 84 557 496 262 983 251 668 902 869 308 584 919 845 972 957 553 573 628 709 879 322 661 536 167 408 564 729 631 354 547 201 138 283 826 886 52 562 259 685 980 450 953 890 802 600 13 625 85 536 664 135 599 885 541 924 464 7 77 633 146 855 582 224 355 336 736 532 704 190 1 479 825 425 641 285 564 627 841 824 738 54 727 851 930 297 896 244 739 392 476 503 955 744 595 742 102 872 597 97 948 25 288 982 598 936 992 908 992 563 235 647 746 472 411 362 490 656 871 957 89 937 526 286 380 806 155 98 352 489 335 497 30 274 88 513 639 638 108 855 73 527 691 286 26 209 298 99 673 482 30 96 190 662 133 96 980 708 99 457 947 28 802 315 787 2 619 216 833 34 449 656 631 984 78 537 104 159 402 961 844 648 580 845 785 701 344 811 319 995 311 438 641 97 342 462 981 186 694 764 214 66 958 2 220 866 553 561 288 337 852 102 799 562 839 350 416 13 593 931 979 325 754 994 399 844 604 98 870 21 316 301 830 950 438 725 269 936 709 891 87 780 831 979 471 595 956 802 413 342 207 674 828 971 753 552 948 983 603 795 44 476 520 639 852 262 179 22 466 410 986 691 892 698 767 631 877 765 878 747 128 430 156 336 540 561 530 392 569 68 40 949 503 100 474 705 933 275 830 935 409 824 331 265 890 871 771 229 328 665 576 666 420 480 53 888 356 68 982 282 150 18 857 449 981 76 816 237 820 549 529 77 488 152 100 817 243 299 323 859 882 645 508 791 389 865 405 830 104 59 716 364 480 890 58 590 535 528 256 730 215 762 279 612 36 174 219 459 506 104 214 566 46 243 344 179 364 93 115 293 466 182 327 284 802 905 767 240 362 76 415 632 883 804 571 478 713 95 591 469 304 674 731 643 732 863 931 32 138 17 232 396 493 914 938 579 604 722 544 251 889 644 922 793 14 109 261 870 152 412 750 800 255 67 98 169 460 709 517 268 450 299 951 840 371 552 974 309 673 960 948 128 94 511 761 155 833 242 698 964 847 32 772 840 137 662 164 803 814 965 219 345 726 118 869 770 440 457 201 942 388 978 353 944 91 622 861 707 460 738 97 895'.split(' ')
# mis2 = '580 979 1039 929 1778 878 1503 1084 479 222 1066 1267 1184 1910 1887 836 1487 1569 1676 819 971 1219 1460 1245 1302 641 758 1234 1570 1177 1503 1817 1510 1201 1588 983 703 972 1360 901 339 1109 938 821 1665 1403 1692 613 710 1200 734 1426 1388 84 779 1437 579 1072 1236 191 1304 1066 849 1468 1562 781 1781 1193 983 868 1458 1339 844 1469 1045 313 1580 1928 1900 798 1393 883 852 1527 1046 1463 666 961 450 824 527 362 1152 746 928 1218 312 507 772 512 286 795 1076 807 1404 830 1102 621 1049 483 1287 1062 641 561 1805 1228 1630 1045 1130 1306 1079 439 1443 880 978 1024 222 1419 849 1189 901 1401 766 606 1910 1079 1393 1448 968 337 1131 1388 994 1645 978 1611 1450 1551 1215 549 1502 1724 1500 1586 839 996 1491 441 488 1396 1583 1465 1508 1643 875 586 876 1091 961 108 1452 574 1638 1105 1344 1155 1155 1642 557 1241 1086 533 1244 1050 432 875 1430 892 1057 1078 565 252 1060 622 1741 1153 1180 1270 934 775 844 948 1125 784 945 1041 648 393 965 318 612 587 543 208 759 509 1086 1672 602 491 1515 1375 1191 686 773 1405 1375 1794 170 249 889 1852 1183 1266 1140 1566 807 370 1022 1162 1055 165 629 1226 718 1250 1211 1526 982 1908 222 1272 988 940 1811 804 977 826 1617 1184 1071 987 1210 658 1330 1331 1035 1483 1167 835'.split(' ')
# mis1 = list(map(int, mis1))
# mis2 = list(map(int, mis2))

# print('sum(mis1)',sum(mis1))
# print('sum(mis2)',sum(mis2))





