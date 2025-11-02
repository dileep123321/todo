# Stage 1: Build the React app using Node
FROM node:18 AS build

WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./

# Install dependencies
RUN npm install --legacy-peer-deps

# Copy all app source code
COPY . .

# ✅ Ensure vite has execute permissions
RUN chmod +x node_modules/.bin/vite

# ✅ Run the build command
RUN npx vite build

# Stage 2: Serve the app using Nginx
FROM nginx:stable-alpine

# Copy built files from build stage to Nginx html directory
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 for container
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
