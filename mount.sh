# sudo kdir /media/mulliganaceous/Mulliganaceous_S;
# sudo mount -t ntfs /dev/sda6 /media/mulliganaceous/Mulliganaceous_S;
# sudo mkdir /media/mulliganaceous/MulligOneDrive;
# sudo mount -t ntfs /dev/sda5 /media/mulliganaceous/MulligOneDrive;
# sudo mkdir /dev/sda4 /media/mulliganaceous/C1;
# sudo mount -t ntfs /dev/sda4 /media/mulliganaceous/C1

# Mount partitions
if ! df | grep -q /dev/nvme0n1p4; then
  udisksctl mount --block-device=/dev/nvme0n1p4
fi
if ! df | grep -q /dev/nvme0n1p5; then
  udisksctl mount --block-device=/dev/nvme0n1p5
fi
if ! df | grep -q /dev/nvme0n1p6; then
  udisksctl mount --block-device=/dev/nvme0n1p6
fi
