document.addEventListener('DOMContentLoaded', function () {
    const showInfoButton = document.querySelector('.button');
    const infoBox = document.getElementById('infoBox');
    const carteiraDropdown = document.getElementById('carteira');

    showInfoButton.addEventListener('click', function () {
        const selectedOption = carteiraDropdown.value;
        let infoText = '';

        if (selectedOption === 'financeiro') {
            infoText = `
                Nome do Fundo: FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS F ACB - FINANCEIRO
                CNPJ do Fundo: 14330038000137
            `;
        } else if (selectedOption === 'comercial') {
            infoText = `
                Nome do Fundo: INVESTCRED FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS
                CNPJ do Fundo: 29226654000110

                Nome do Fundo: HAVAN FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS
                CNPJ do Fundo: 12817329000129

                Nome do Fundo: APOLO FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS
                CNPJ do Fundo: 34218625000146
            `;
        } else if (selectedOption === 'industrial') {
            infoText = `
                Nome do Fundo: FIDC - INSUMOS BÁSICOS DA INDÚSTRIA PETROQUÍMICA
                CNPJ do Fundo: 13850522000124

                Nome do Fundo: EUV SP1 FUNDO DE INVESTIMENTO EM DIREITOS CREDITORIOS
                CNPJ do Fundo: 44229197000100

                Nome do Fundo: CATERPILLAR FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS DO SEGMENTO INDUSTRIAL II
                CNPJ do Fundo: 5754060000113
            `;
        } else if (selectedOption === 'servicos') {
            infoText = `
                Nome do Fundo: FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS XPCE INFRA
                CNPJ do Fundo: 31216543000174

                Nome do Fundo: FOR-TE FIDC
                CNPJ do Fundo: 6182371000118

                Nome do Fundo: CATERPILLAR FUNDO DE INVESTIMENTO EM DIREITOS CREDITÓRIOS DO SEGMENTO INDUSTRIAL II
                CNPJ do Fundo: 5754060000113
            `;
        }

        infoBox.textContent = infoText;
    });
});