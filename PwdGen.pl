use strict;
use warnings;
use List::Util 'shuffle';

my $password_file = "passwords.txt";

# Function to generate password
sub generate_password {
    my ($length, $use_numbers, $use_symbols) = @_;
    
    # Define character sets
    my @lowercase = ('a'..'z');
    my @uppercase = ('A'..'Z');
    my @numbers   = ('0'..'9');
    my @symbols   = ('!', '@', '#', '$', '%', '^', '&', '*');
    
    # Build the final character set
    my @all_chars = (@lowercase, @uppercase);
    push @all_chars, @numbers if $use_numbers;
    push @all_chars, @symbols if $use_symbols;
    
    # Ensure at least one character from each enabled category
    my @password;
    push @password, $lowercase[rand @lowercase];
    push @password, $uppercase[rand @uppercase];
    push @password, $numbers[rand @numbers] if $use_numbers;
    push @password, $symbols[rand @symbols] if $use_symbols;
    
    # Fill the rest of the password length with random characters
    push @password, (shuffle(@all_chars))[0..($length - @password) - 1];
    
    return join '', shuffle(@password);
}

# Function to store password
sub store_password {
    my ($name, $password) = @_;
    open(my $fh, '>>', $password_file) or die "Could not open file: $!";
    print $fh "$name: $password\n";
    close($fh);
}

# Function to view stored passwords
sub view_passwords {
    if (-e $password_file) {
        open(my $fh, '<', $password_file) or die "Could not open file: $!";
        print "\nStored Passwords:\n";
        while (my $line = <$fh>) {
            print $line;
        }
        close($fh);
    } else {
        print "\nNo stored passwords found.\n";
    }
}

# Main loop to allow continuous interaction
while (1) {
    print "\nChoose an option:\n";
    print "1. Generate a new password\n";
    print "2. View saved passwords\n";
    print "3. Exit\n";
    print "Enter your choice: ";
    my $choice = <STDIN>;
    chomp($choice);
    
    if ($choice == 1) {
        # Get user input for password generation
        print "Enter password length: ";
        my $length = <STDIN>;
        chomp($length);
        $length = 12 if $length !~ /^\d+$/ || $length < 4;  # Default to 12, min 4

        print "Include numbers? (y/n): ";
        my $use_numbers = <STDIN> =~ /^y/i;

        print "Include symbols? (y/n): ";
        my $use_symbols = <STDIN> =~ /^y/i;

        # Generate password
        my $password = generate_password($length, $use_numbers, $use_symbols);
        print "Generated Password: $password\n";

        # Store password if the user wants
        print "Would you like to save this password? (y/n): ";
        if (<STDIN> =~ /^y/i) {
            print "Enter a name for this password: ";
            my $name = <STDIN>;
            chomp($name);
            store_password($name, $password);
            print "Password saved!\n";
        }
    } 
    elsif ($choice == 2) {
        view_passwords();
    } 
    elsif ($choice == 3) {
        print "Exiting...\n";
        last;
    } 
    else {
        print "Invalid choice, please try again.\n";
    }
}
