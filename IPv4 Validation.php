# IPv4 Validation PHP
# Author: Sandro Zappulla
# Github: @SandroZappulla
# version: v1.0

// bedingung: Wenn submittet wurde
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    // VARIABLES
    $ipv4 = htmlspecialchars($_POST['ipv4']);

    echo "Objekt_name: ", $object_name, "<br>";
    echo "IPv4: ", $ipv4, "<br>";
    echo "IPv6: ", $ipv6;
    echo "<br><br><br><br><br>";


    // VALIDATION

    // *** IPV4-ADDRESS ***
    // error_msg
    $error_empty = "Eingabe darf nicht leer sein!<br>";
    $error_ipv4_pattern = "Das Pattern der IPv4-Adresse stimmt nicht ein!<br>";
    $error_length = "Die Länge muss mind. 7 Zeichen und max 15 Zeichen Lang sein!<br>";
    $error_first_char_is_digit = "Erstes Zeichen muss eine Zahl enthalten!<br>";
    $error_digits_or_dots = "Nur Zahlen oder Punkte Verwenden!<br>";
    $error_amount_dots = "Es müssen exakt 3 Punkte enthalten sein.<br>";
    $error_unvalid_digit = "Eine Verwendetes Oktett besitzt nicht eine Zahlen range von (0-255)! <br>";

    // Counter
    $char_counter = 0;

    // Überprüfe: Ob Leerer Eintrag (Auch für Objektname und IPv6 Adresse)
    if(empty($object_name) || (empty($ipv4)) || (empty($ipv6))) {
        echo $error_empty;
    }



    // Überprüfe: Länge
    $ipv4_length = strlen($ipv4);
    if ($ipv4_length < 7 || $ipv4_length > 15){
        echo $error_length;
    }



    // Überprüfe: Anzahl der Punkte
    $dot_count = substr_count($ipv4,".");

    if ($dot_count != 3){
        echo $error_amount_dots;
    }



    // Überprüfe: Zahl oder Punkt vorhanden
    do{
        if (is_numeric($ipv4[$char_counter]) || $ipv4[$char_counter] == "."){
        }
        else {
            echo $error_digits_or_dots;
        }

        $char_counter+=1;  
    } while($char_counter < $ipv4_length);



    // RegEx Pattern Überprüfen
    // Pattern 
    $ipv4_pattern = '/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/';
    
    if (preg_match($ipv4_pattern, $ipv4) == 0){ // Rückgabewert bei preg_match() ist 0 wenn Falsch und 1 wenn richtig
        echo $error_ipv4_pattern;
    }



    // Überprüfe ob erstes Zeichen eine Zahl ist
    $first = $ipv4[0];
    if (!is_numeric($first)){
        echo $error_first_char_is_digit;
    }

    // Überprüfung: Validierung einer einzelnen Zahl (Zwischen 0-255)
    $oktett = explode(".", $ipv4);

    $counter_single_digit = 0;

    do {
        if ($oktett[$counter_single_digit] < 0 || $oktett[$counter_single_digit] > 255){
            $unvalid_digit +=1;
            echo $error_unvalid_digit;
            break;
        }
        $counter_single_digit +=1;
    } while ($counter_single_digit < $dot_count+1);
}
// Wenn nicht submittet wurde direkt zurücksenden zur index.php #SECURITY
else {
    header("Location: index.php");
}
