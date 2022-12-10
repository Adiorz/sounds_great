FROM node:latest as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
RUN npm run build

FROM pierrezemb/gostatic as production-stage
COPY --from=build-stage /app/dist /srv/http/
