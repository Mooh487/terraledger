# TerraGold Frontend Dockerfile
FROM node:18-alpine as builder

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy built assets from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Create non-root user
RUN addgroup -g 1001 -S nodejs \
    && adduser -S terraledger -u 1001

# Set ownership
RUN chown -R terraledger:nodejs /usr/share/nginx/html \
    && chown -R terraledger:nodejs /var/cache/nginx \
    && chown -R terraledger:nodejs /var/log/nginx \
    && chown -R terraledger:nodejs /etc/nginx/conf.d \
    && touch /var/run/nginx.pid \
    && chown -R terraledger:nodejs /var/run/nginx.pid

USER terraledger

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000 || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
