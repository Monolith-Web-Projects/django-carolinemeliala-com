-- Insert mock products data into PostgreSQL
-- Run this after creating and migrating your Django models

INSERT INTO dmusemagz_shop_product (
    productId, 
    productCategory, 
    productName, 
    productColor, 
    productImage, 
    productSize, 
    productQuantity, 
    productDescription, 
    productPrice
) VALUES 
('bag-001', 'Bags', 'Quilted Leather Shoulder Bag', 'Ivory', 'https://www.net-a-porter.com/variants/images/46376663162863533/in/w358_q60.jpg', 'One Size', 1, 'An elegant ivory shoulder bag crafted from supple quilted leather with gold-tone accents. A timeless companion for every look.', 450.00),

('bag-002', 'Bags', 'Mini Top-Handle Bag', 'Soft Beige', 'https://www.net-a-porter.com/variants/images/46376663162881746/in/w358_q60.jpg', 'Mini', 1, 'A structured mini bag with a vintage-inspired silhouette, designed in soft beige and finished with a sculpted handle.', 395.00),

('bag-003', 'Bags', 'Chain-Detail Crossbody', 'Dusty Pink', 'https://www.net-a-porter.com/variants/images/1647597359753800/in/w358_q60.jpg', 'Standard', 1, 'A compact crossbody bag with polished chain hardware and a softly textured finish for modern femininity.', 520.00),

('mini-001', 'Mini Dress', 'Floral Ruffle Mini Dress', 'Lilac Print', 'https://www.net-a-porter.com/variants/images/1647597304983283/ou/w2000_q60.jpg', 'S', 1, 'A breezy mini dress with delicate ruffles and a romantic floral print, ideal for summer garden parties.', 360.00),

('mini-002', 'Mini Dress', 'Silk Wrap Mini Dress', 'Champagne', 'https://www.net-a-porter.com/variants/images/1647597349574119/ou/w2000_q60.jpg', 'M', 1, 'Cut from luxurious silk, this wrap mini dress features a deep neckline and tie waist for a refined evening look.', 520.00),

('dress-001', 'Dress', 'Long-Sleeve Satin Gown', 'Midnight Blue', 'https://www.net-a-porter.com/variants/images/1647597317632698/ou/w2000_q60.jpg', 'M', 1, 'An ethereal satin gown with a high neckline, long sleeves, and floor-length hemline in a deep, moody tone.', 980.00),

('dress-002', 'Dress', 'Structured Evening Dress', 'Crimson Red', 'https://www.net-a-porter.com/variants/images/1647597317850984/ou/w2000_q60.jpg', 'S', 1, 'A dramatic silhouette with cinched waist and architectural folds, crafted in rich crimson for standout events.', 840.00),

('dress-003', 'Dress', 'Sleeveless Crepe Gown', 'Off White', 'https://www.net-a-porter.com/variants/images/46376663162843734/ou/w2000_q60.jpg', 'L', 1, 'Understated elegance in a sleeveless crepe gown with minimalist lines and soft off-white tone.', 750.00);