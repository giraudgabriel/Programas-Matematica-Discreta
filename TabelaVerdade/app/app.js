var app = angular.module("app", []);
app.controller("TabelaController", function ($scope) {
    $scope.gerar = () => {
        $scope.tabelas = [];

        for (let index = -1; index < $scope.qtdElementos; index++) {

            if (index == 0) {
                $scope.tabelas.push({
                    nome: 'p',
                    valores: [true, true, false, false]
                });
            } else if(index==1) {
                $scope.tabelas.push({
                    nome: 'q',
                    valores: [true, false, true, false]
                });
            }
        }
        console.log($scope.tabelas);
    };

    $scope.negar = () =>
    {
        $scope.tabelas.forEach(e => {
            let negados = [];
            for (let i = 0; i < e.valores.length; i++) {
                negados.push(!e.valores[i]); 
            }          
            $scope.tabelas.push({nome: '~'+e.nome,valores:negados});
        });
    };


});