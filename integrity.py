def verify_integrity(data_packet):
    return data_packet == data_packet[::-1]

packet = input("Enter data packet to verify: ")
if verify_integrity(packet):
    print("INTEGRITY VERIFIED: Data is a palindrome — not corrupted.")
else:
    print("INTEGRITY FAILED: Data has been altered.")