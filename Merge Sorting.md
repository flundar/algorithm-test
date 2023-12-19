Verilen dizinin Merge Sort ile sıralama aşamaları şu şekildedir:

Verilen dizi: [16, 21, 11, 8, 12, 22]

Adım: [16, 21, 11], [8, 12, 22] (Diziyi iki eşit parçaya böleriz)
Adım: [16, 21], [11], [8, 12], [22] (Her iki parçayı da tekrar ikiye böleriz)
Adım: [16], [21], [11], [8], [12], [22] (Her parçayı tek elemanlı alt dizilere böleriz)
Adım: [16, 21], [8, 11], [12, 22] (Çiftler halinde birleştiririz)
Adım: [8, 11, 16, 21], [12, 22] (Son iki çifti birleştiririz)
Adım: [8, 11, 12, 16, 21, 22] (Son iki parçayı birleştiririz)
Dizi artık sıralanmıştır. Merge Sort'un Big-O gösterimi O(n log n)'dir.
