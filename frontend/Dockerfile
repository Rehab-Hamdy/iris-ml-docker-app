# Use Nginx as frontend server
FROM nginx:alpine

# Copy frontend files to default Nginx path
COPY index.html /usr/share/nginx/html/index.html
COPY style.css /usr/share/nginx/html/style.css

# Expose port
EXPOSE 80
