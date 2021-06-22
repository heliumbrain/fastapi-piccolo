FROM mhart/alpine-node:16

# install dependencies
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN npm install -g pnpm
RUN pnpm install

# Copy all local files into the image.
COPY . .

RUN pnpm build

###
# Only copy over the Node pieces we need
# ~> Saves 35MB
###
FROM mhart/alpine-node:slim-16

WORKDIR /app
COPY --from=0 /app .
COPY . .

EXPOSE 3000
CMD ["node", "./build"]