/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package robot;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/**
 *
 * @author ramo828
 */
public class comm {

    private static String yekun;
    private static final File file = new File("autoMessage.config");
    private static final String beginConfig = "#<CONFIG";
    private static final String endConfig = "ENDCONFIG#>";


    public static String config(int index) throws FileNotFoundException, IOException {

        FileReader fileReader = new FileReader(file);
        String line;
        try (BufferedReader br = new BufferedReader(fileReader)) {
            while ((line = br.readLine()) != null) {
                
                  if(line.startsWith(beginConfig) && line.endsWith(endConfig)){
                String[] result = line.split(":");
                yekun = result[index];
                  }
                
            }
        }
        return yekun;
    }

    public static void writeConfig(
            int c1,
            int c2,
            int c3,
            int c4,
            int c5,
            int c6,
            int c7,
            int c8,
            int c9,
            int c10,
            int c11,
            int c12) throws IOException {
        

        String conf = "#Ayarlar burdan deyisilecek\n"
                + "#<CONFIG :"+
                c1+":"+
                c2+":"+
                c3+":"+
                c4+":"+
                c5+":"+
                c6+":"+
                c7+":"+
                c8+":"+
                c9+":"+
                c10+":"+
                c11+":"+
                c12+
                ": ENDCONFIG#>\n"+
                "#1 Acilisda gozleme ms\n" +
"#2 Yeni tab acma zamani ms\n" +
"#3 Adresi daxil etme zamani ms\n" +
"#4 Enteri klikleme zamani s\n" +
"#5 Mesajlari secme zamani ms\n" +
"#6 Kopyalama zamani ms\n" +
"#7 Kopyalama sonrasi gozleme ms\n" +
"\n" +
"# ms - milisaniye (1000ms - 1san)\n" +
"# s - san (1 san - 1000ms)\n" +
"#\n" +
"#8 Yeni mesaj gondermeden once gozleme zamani ms\n" +
"#9 Yeni Mesaj tabindan sonra gozleme ms\n" +
"#10 Kontakt adi yazma sureti ms\n" +
"#11 kontakta daxil olduqdan sonraki gozleme zamani s\n" +
"#12 Mesaji kopyaladiqdan sonraki gozleme zamani s\n";

        if (!file.exists()) {
            file.createNewFile();
        }

        FileWriter fileWriter = new FileWriter(file, false);
        BufferedWriter bWriter = new BufferedWriter(fileWriter);
        bWriter.write(conf);
        bWriter.close();

    }
    
}
