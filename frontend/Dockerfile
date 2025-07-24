# --- Etapa 1: Build da Aplicação React ---
# Usamos a imagem oficial do Node.js com uma versão LTS para estabilidade.
# 'AS builder' nomeia esta etapa para que possamos referenciá-la mais tarde.
FROM node:20-alpine AS builder

# Define o diretório de trabalho dentro do contêiner.
WORKDIR /app

# Copia os arquivos de configuração de pacotes (package.json e package-lock.json) primeiro.
# Isso permite que o Docker utilize o cache da camada para 'npm install'.
# Se apenas esses arquivos mudarem, o 'npm install' não será executado novamente.
COPY package*.json ./

# Instala as dependências do projeto.
RUN npm install

# Copia o restante do código fonte da aplicação para o diretório de trabalho.
# O ponto '.' no final significa "copiar tudo do diretório atual do host para o diretório de trabalho do contêiner".
COPY . .

# Executa o comando de build do React.
# Por padrão, muitas ferramentas de build (como Create React App) geram o build em um diretório chamado 'build'.
# Se o seu projeto gera em 'dist' (ex: Vite, Parcel), ajuste a linha na próxima etapa.
RUN npm run build

# --- Etapa 2: Servir com Nginx ---
# Usamos a imagem oficial do Nginx em sua versão 'alpine' para uma imagem final menor.
FROM nginx:alpine

# Remove a configuração padrão do Nginx para evitar conflitos e usar a nossa.
RUN rm -rf /etc/nginx/conf.d/* /usr/share/nginx/html/*

# Copia os arquivos de build da aplicação React da etapa 'builder' para o diretório de serviço do Nginx.
# ATENÇÃO: Verifique se o diretório de build do seu projeto React é 'build'. Se for 'dist', altere '/app/build' para '/app/dist'.
COPY --from=builder /app/dist /usr/share/nginx/html

# Copia nosso arquivo de configuração Nginx personalizado para o local correto.
# Certifique-se de que seu 'nginx.conf' esteja na mesma pasta do Dockerfile.
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expõe a porta 80 do contêiner. Esta é a porta padrão para HTTP.
EXPOSE 80

# Comando que será executado quando o contêiner for iniciado.
# '-g "daemon off;"' garante que o Nginx execute em primeiro plano, o que é essencial para o Docker.
CMD ["nginx", "-g", "daemon off;"]