$name_of_cat = "Garfield";
sub print_the_name_of_the_cat{
    print "$name_of_cat\n";
}
sub dynamic_cat{
    local $name_of_cat = "Mr. Jinx";
    print_the_name_of_the_cat();
}
sub static_cat{
    my $name_of_cat = "Salem";
    print_the_name_of_the_cat();
}
sub print_cat(){
    print "The name of the cat in the Dynamic Scope is ";
    dynamic_cat();
    print "The name of the cat in the Static Scope is ";
    static_cat();
}
print_cat();
