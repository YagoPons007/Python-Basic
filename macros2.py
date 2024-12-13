function enviaCheckList() {
  var fulla = SpreadsheetApp.openById('TU_ID_DE_HOJA_DE_CALCULO');  // Substitueix amb l'ID de la teva fulla de càlcul
  var rang = fulla.getSheetByName('Hoja1').getDataRange();  // Suposant que la llista està a la fulla 'Hoja1'
  var dades = rang.getValues();  // Obté tots els valors de la fulla
  
  var doc = DocumentApp.openById('TU_ID_DE_DOCUMENTO');  // Substitueix amb l'ID del teu document
  var cos = doc.getBody().getText();  // Obté el text del document

  for (var i = 1; i < dades.length; i++) {  // Comença des de la fila 1 per saltar el capçalera
    var nom = dades[i][0];  // Nom de la persona (columna A)
    var correu = dades[i][1];  // Correu electrònic de la persona (columna B)
    
    var assumpte = 'CheckList de Grup';  // Assumpte del correu
    var cosEmail = 'Hola ' + nom + ',\n\n' + 
                    'Aquí tens el checklist de l\'activitat:\n\n' + 
                    cos + '\n\n' +
                    'Si us plau, marca els items completats.\n\n' +
                    'Salutacions,\nEl teu company';  // Cos del missatge

    MailApp.sendEmail(correu, assumpte, cosEmail);
  }

  Logger.log('CheckList enviat a tots els companys.');
}
