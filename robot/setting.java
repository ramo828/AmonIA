/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package robot;

import java.awt.Color;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.UnsupportedLookAndFeelException;
import robot.comm;

/**
 *
 * @author ramo828
 */
public class setting extends javax.swing.JFrame {

    /**
     * Creates new form setting
     */
    public setting() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jButton1 = new javax.swing.JButton();
        lab = new javax.swing.JLabel();
        s11 = new javax.swing.JSpinner();
        s6 = new javax.swing.JSpinner();
        s4 = new javax.swing.JSpinner();
        s3 = new javax.swing.JSpinner();
        s2 = new javax.swing.JSpinner();
        s1 = new javax.swing.JSpinner();
        s5 = new javax.swing.JSpinner();
        s10 = new javax.swing.JSpinner();
        s9 = new javax.swing.JSpinner();
        s7 = new javax.swing.JSpinner();
        s8 = new javax.swing.JSpinner();
        s12 = new javax.swing.JSpinner();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        jLabel9 = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        jLabel11 = new javax.swing.JLabel();
        jLabel12 = new javax.swing.JLabel();
        jLabel13 = new javax.swing.JLabel();
        jLabel14 = new javax.swing.JLabel();
        jLabel15 = new javax.swing.JLabel();
        jLabel16 = new javax.swing.JLabel();
        jLabel17 = new javax.swing.JLabel();
        jLabel18 = new javax.swing.JLabel();
        jLabel19 = new javax.swing.JLabel();
        jLabel20 = new javax.swing.JLabel();
        jLabel21 = new javax.swing.JLabel();
        jLabel22 = new javax.swing.JLabel();
        jLabel23 = new javax.swing.JLabel();
        jLabel24 = new javax.swing.JLabel();
        jLabel25 = new javax.swing.JLabel();
        save = new javax.swing.JButton();
        reset = new javax.swing.JButton();
        exit1 = new javax.swing.JButton();
        jLabel1 = new javax.swing.JLabel();
        jLabel26 = new javax.swing.JLabel();

        jButton1.setText("jButton1");

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        lab.setFont(new java.awt.Font("Cantarell", 1, 26)); // NOI18N
        lab.setText("AvtoMesaj Incə ayarlar");

        s11.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        s6.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        s4.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        s3.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        s2.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        s1.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        s5.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        s10.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        s9.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        s7.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        s8.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        s12.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N

        jLabel2.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel2.setText("Yeni tab açma zamanı:");

        jLabel3.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel3.setText("Açılışda gözləmə: ");

        jLabel4.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel4.setText("Adresi daxil etmə zamanı:");

        jLabel5.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel5.setText("Mesajları secmə zamanı:");

        jLabel6.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel6.setText("Enteri klikləmə zamanı:");

        jLabel7.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel7.setText("Kopyalama zamanı:");

        jLabel8.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel8.setText("Yeni Mesaj tabından sonra gözləmə");

        jLabel9.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel9.setText("Yeni mesaj göndərmədən öncə gözləmə zamanı");

        jLabel10.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel10.setText("Kontakt adı yazma sürəti");

        jLabel11.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel11.setText("Mesajı yapışdırdıqdan sonrakı gözləmə zamanı");

        jLabel12.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel12.setText("kontakta daxil olduqdan sonrakı gözləmə zamanı");

        jLabel13.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel13.setText("Kopyalama sonrası gözləmə");

        jLabel14.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel14.setText("ms");

        jLabel15.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel15.setText("ms");

        jLabel16.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel16.setText("san");

        jLabel17.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel17.setText("s");

        jLabel18.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel18.setText("ms");

        jLabel19.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel19.setText("ms");

        jLabel20.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel20.setText("ms");

        jLabel21.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel21.setText("ms");

        jLabel22.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel22.setText("ms");

        jLabel23.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel23.setText("ms");

        jLabel24.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel24.setText("s");

        jLabel25.setFont(new java.awt.Font("Cantarell", 1, 18)); // NOI18N
        jLabel25.setText("s");

        save.setFont(new java.awt.Font("Cantarell", 1, 20)); // NOI18N
        save.setText("Yadda saxla");
        save.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                saveActionPerformed(evt);
            }
        });

        reset.setFont(new java.awt.Font("Cantarell", 1, 20)); // NOI18N
        reset.setText("Ayarları sıfırla");
        reset.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                resetActionPerformed(evt);
            }
        });

        exit1.setFont(new java.awt.Font("Cantarell", 1, 20)); // NOI18N
        exit1.setText("Çıx");
        exit1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                exit1ActionPerformed(evt);
            }
        });

        jLabel1.setForeground(new java.awt.Color(255, 51, 51));
        jLabel1.setText("Mesaj göndərmə");

        jLabel26.setForeground(new java.awt.Color(255, 51, 51));
        jLabel26.setText("Mesaj kopyalama");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(50, 50, 50)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel5)
                                    .addComponent(jLabel7)
                                    .addComponent(jLabel3)
                                    .addComponent(jLabel6)
                                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                        .addComponent(jLabel26)
                                        .addComponent(jLabel2)))
                                .addGap(22, 22, 22))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                .addContainerGap()
                                .addComponent(jLabel4)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)))
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(s5, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(s4, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(s3, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(s2, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(s6, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(s1, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel14)
                                    .addComponent(jLabel15)
                                    .addComponent(jLabel16)
                                    .addComponent(jLabel17)
                                    .addComponent(jLabel19)
                                    .addComponent(jLabel18))
                                .addGap(36, 36, 36)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel9)
                                    .addComponent(jLabel11)
                                    .addComponent(jLabel10)
                                    .addComponent(jLabel12)
                                    .addComponent(jLabel8)
                                    .addComponent(jLabel13))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 85, Short.MAX_VALUE)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(s12, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(jLabel24))
                                    .addGroup(layout.createSequentialGroup()
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                                .addComponent(s8, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE)
                                                .addComponent(s7, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE))
                                            .addComponent(s11, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE)
                                            .addComponent(s10, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE)
                                            .addComponent(s9, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE))
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(jLabel25)
                                            .addComponent(jLabel23)
                                            .addComponent(jLabel22)
                                            .addComponent(jLabel21)
                                            .addComponent(jLabel20)))))
                            .addGroup(layout.createSequentialGroup()
                                .addGap(186, 186, 186)
                                .addComponent(jLabel1)
                                .addGap(0, 0, Short.MAX_VALUE))
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(save)
                                .addGap(18, 18, 18)
                                .addComponent(exit1)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addComponent(reset)
                                .addGap(101, 101, 101))))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(333, 333, 333)
                        .addComponent(lab)
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(lab)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel1)
                    .addComponent(jLabel26))
                .addGap(2, 2, 2)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 28, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jLabel2, javax.swing.GroupLayout.DEFAULT_SIZE, 33, Short.MAX_VALUE)
                        .addGap(239, 239, 239))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(s7, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel20))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(s8, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel21))
                                .addGap(12, 12, 12)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(s9, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel22))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(s10, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel12)
                                    .addComponent(jLabel23))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(s11, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel11)
                                    .addComponent(jLabel25))
                                .addGap(12, 12, 12)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(jLabel9)
                                    .addComponent(jLabel24)
                                    .addComponent(s12, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                            .addComponent(jLabel13)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addComponent(jLabel14)
                                    .addComponent(s1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(s2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel15)
                                    .addComponent(jLabel8))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(s3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel4, javax.swing.GroupLayout.PREFERRED_SIZE, 28, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel16)
                                    .addComponent(jLabel10))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(s4, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel6)
                                    .addComponent(jLabel17))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(s5, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel5)
                                    .addComponent(jLabel19))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(s6, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel7)
                                    .addComponent(jLabel18))))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(save)
                            .addComponent(exit1)
                            .addComponent(reset))
                        .addGap(26, 26, 26))))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void saveActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_saveActionPerformed
        comm c = new comm();
        try {
            c.writeConfig(
                    (Integer) s1.getValue(),
                    (Integer) s2.getValue(),
                    (Integer) s3.getValue(),
                    (Integer) s4.getValue(),
                    (Integer) s5.getValue(),
                    (Integer) s6.getValue(),
                    (Integer) s7.getValue(),
                    (Integer) s8.getValue(),
                    (Integer) s9.getValue(),
                    (Integer) s10.getValue(),
                    (Integer) s11.getValue(),
                    (Integer) s12.getValue());
            lab.setForeground(Color.green);
            lab.setText(("Qeyd edildi !"));
        } catch (IOException ex) {
            Logger.getLogger(setting.class.getName()).log(Level.SEVERE, null, ex);
        }
    }//GEN-LAST:event_saveActionPerformed

    private void resetActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_resetActionPerformed
        comm c = new comm();
        try {
            c.writeConfig(100,
                    100,
                    100,
                    2,
                    300,
                    500,
                    200,
                    1100,
                    200,
                    1,
                    1,
                    0);
            loadConfig();
        } catch (IOException ex) {
            Logger.getLogger(setting.class.getName()).log(Level.SEVERE, null, ex);
        }
        lab.setForeground(Color.red);
        lab.setText("Ayarlar sıfırlandı !");        
    }//GEN-LAST:event_resetActionPerformed

    private void exit1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_exit1ActionPerformed
        System.exit(0);    }//GEN-LAST:event_exit1ActionPerformed

    /**
     * @param args the command line arguments
     */
    private static void loadConfig() throws IOException {
        comm c = new comm();
        s1.setValue(Integer.parseInt(c.config(1)));
        s2.setValue(Integer.parseInt(c.config(2)));
        s3.setValue(Integer.parseInt(c.config(3)));
        s4.setValue(Integer.parseInt(c.config(4)));
        s5.setValue(Integer.parseInt(c.config(5)));
        s6.setValue(Integer.parseInt(c.config(6)));
        s7.setValue(Integer.parseInt(c.config(7)));
        s8.setValue(Integer.parseInt(c.config(8)));
        s9.setValue(Integer.parseInt(c.config(9)));
        s10.setValue(Integer.parseInt(c.config(10)));
        s11.setValue(Integer.parseInt(c.config(11)));
        s12.setValue(Integer.parseInt(c.config(12)));
        
    }
    
    public static void main(String args[]) throws IOException {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
            if ("Nimbus".equals(info.getName())) {
                try {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                } catch (ClassNotFoundException ex) {
                    Logger.getLogger(setting.class.getName()).log(Level.SEVERE, null, ex);
                } catch (InstantiationException ex) {
                    Logger.getLogger(setting.class.getName()).log(Level.SEVERE, null, ex);
                } catch (IllegalAccessException ex) {
                    Logger.getLogger(setting.class.getName()).log(Level.SEVERE, null, ex);
                } catch (UnsupportedLookAndFeelException ex) {
                    Logger.getLogger(setting.class.getName()).log(Level.SEVERE, null, ex);
                }
                break;
            }
        }

        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new setting().setVisible(true);
                try {
                    loadConfig();
                } catch (IOException ex) {
                    Logger.getLogger(setting.class.getName()).log(Level.SEVERE, null, ex);
                }
                
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton exit1;
    private javax.swing.JButton jButton1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel12;
    private javax.swing.JLabel jLabel13;
    private javax.swing.JLabel jLabel14;
    private javax.swing.JLabel jLabel15;
    private javax.swing.JLabel jLabel16;
    private javax.swing.JLabel jLabel17;
    private javax.swing.JLabel jLabel18;
    private javax.swing.JLabel jLabel19;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel20;
    private javax.swing.JLabel jLabel21;
    private javax.swing.JLabel jLabel22;
    private javax.swing.JLabel jLabel23;
    private javax.swing.JLabel jLabel24;
    private javax.swing.JLabel jLabel25;
    private javax.swing.JLabel jLabel26;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JLabel lab;
    private javax.swing.JButton reset;
    private static javax.swing.JSpinner s1;
    private static javax.swing.JSpinner s10;
    private static javax.swing.JSpinner s11;
    private static javax.swing.JSpinner s12;
    private static javax.swing.JSpinner s2;
    private static javax.swing.JSpinner s3;
    private static javax.swing.JSpinner s4;
    private static javax.swing.JSpinner s5;
    private static javax.swing.JSpinner s6;
    private static javax.swing.JSpinner s7;
    private static javax.swing.JSpinner s8;
    private static javax.swing.JSpinner s9;
    private javax.swing.JButton save;
    // End of variables declaration//GEN-END:variables
}
